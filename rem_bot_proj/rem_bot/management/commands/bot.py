from datetime import datetime
from django.core.management.base import BaseCommand
from django.conf import settings
from rembg import remove
from aiogram import Bot, Dispatcher, executor, types
from PIL import Image,ImageFilter
import os
import sqlite3





class Command(BaseCommand):
    help = 'remover_bot'

    def handle(self, *args, **options):

        bot = Bot(token=settings.API_TOKEN)
        dp = Dispatcher(bot)
        bt=[['Получить фото без фона','Получить портретное фото']]

        def lol(id,name,user):
            connector = sqlite3.connect(settings.BASE_DIR/'db.sqlite3')
            cursor = connector.cursor()
            try:
                cursor.execute('''INSERT INTO rem_bot_profile(name,external_id,username) values(?,?,?) ''',(name, id, user))
            except:
                cursor.execute('''update rem_bot_profile SET name = ?, username = ? WHERE external_id = ?''', (name,user,id))
                cursor.execute('''update rem_bot_profile SET count = count + 1 WHERE external_id = ?''', (id,))

            connector.commit()

        @dp.message_handler(commands=['start'])
        async def send_hello(message: types.Message):

            await message.answer('Привет! Я Remover_Bot и я создан для того, что бы удалять задний фон на фото. Отправь мне фото '
                                 'и я удалю задний фон или размою его')

        @dp.message_handler(commands=['help'])
        async def send_hello(message: types.Message):
            await message.answer('Всё очень просто! Отправьте мне фото')

        @dp.message_handler(content_types='photo')
        async def take_photo(message: types.Message):
            button = types.ReplyKeyboardMarkup(keyboard=bt, resize_keyboard=True)
            await message.answer("Ваше фото готово. Нажмите кнопку, чтобы получить ваше фото документом",reply_markup=button)\
                ,set_stat()
            await message.photo[-1].download(f'media/{message.from_user.id}.jpg'), remove_bg(message.from_user.id), \
            portrait(message.from_user.id)
            await paste(message.from_user.id)
            await lol(message.from_user.id, message.from_user.first_name, message.from_user.username)


        def set_stat():
            connector = sqlite3.connect(settings.BASE_DIR/'db.sqlite3')
            cursor = connector.cursor()
            date = str(datetime.now())
            date = date[0:10]
            try:
                cursor.execute('''INSERT into rem_bot_stat(date,count) values (?,1)''',(date,))
            except:
                cursor.execute('''update rem_bot_stat SET count = count + 1 WHERE date = ?''', (date,))
            connector.commit()


        def portrait(id):
            file=f"media/{id}.jpg"
            file_blur=f"media/{id}_blur.png"
            with Image.open(file) as img:
                img.load()
                image=img.filter(ImageFilter.GaussianBlur(5))
                image.save(file_blur)

        def paste(id):
            file_blur = Image.open(f"media/{id}_blur.png")
            file_cut = Image.open(f"media/{id}.png")
            file_blur.paste(im=file_cut,mask=file_cut)
            file_blur.save(f"media/{id}_blur.png")

        def remove_bg(id):
            input_path = f"media/{id}.jpg"
            output_path = f"media/{id}.png"

            with open(input_path, 'rb') as i:
                with open(output_path, 'wb') as o:
                    input = i.read()
                    output = remove(input)
                    o.write(output)

        @dp.message_handler(regexp='Получить портретное фото')
        async def send_photo(message: types.Message):
            markup = types.ReplyKeyboardRemove()
            with open(f'media/{message.from_user.id}_blur.png', 'rb') as ph:
                await bot.send_document(chat_id=message.chat.id, document=ph)
                await message.answer('Спасибо, что воспользовались нашим сервисом!',reply_markup=markup),os.remove(f'media/{message.from_user.id}.png'),os.remove(f'media/{message.from_user.id}.jpg'),
                os.remove(f'media/{message.from_user.id}_blur.png')

        @dp.message_handler(regexp='Получить фото без фона')
        async def send_photo(message: types.Message):
            markup = types.ReplyKeyboardRemove()
            with open(f'media/{message.from_user.id}.png', 'rb') as ph:
                await bot.send_document(chat_id=message.chat.id, document=ph)
                await message.answer('Спасибо, что воспользовались нашим сервисом!',reply_markup=markup),os.remove(f'media/{message.from_user.id}.png'),os.remove(f'media/{message.from_user.id}.jpg'),
                os.remove(f'media/{message.from_user.id}_blur.png')

        executor.start_polling(dp, skip_updates=True)

