# remover_bot-django
Даннный бот используется для удаления/размытия заднего фона. Пользовтель получает файлы вида id.png/id_blur.png, где id - id пользователя телеграмм. Все данные записываются в базу данных и отображаются через админ-панель django. Разработан студентами Иванниковым Виктором МКИС23 и Соловьевым Артемом МКИС23 Для запуска бота вписать в терминал python manage.py bot. Для запуска админ-панели вписать в терминал python manage.py runserver. Для работы требуется python >3.7 <3.11. Используемые библиотеки Django, rembg, matplotlib, aiogram