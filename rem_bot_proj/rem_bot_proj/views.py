import matplotlib.pyplot as plt
import matplotlib
from django.http import HttpResponse
from django.conf import settings
from django.template import loader
from io import StringIO
import sqlite3
from datetime import datetime
matplotlib.use('Agg')


def generate_graph():
    conn = sqlite3.connect(settings.BASE_DIR / 'db.sqlite3')
    date = str(datetime.now())
    date = date[0:10]
    cursor = conn.execute('SELECT date, count FROM rem_bot_stat where date<=? ORDER BY date DESC LIMIT 5', (date,))

    dates = []
    counts = []
    for row in cursor:
        dates.append(row[0])
        counts.append(row[1])
    dates = dates[::-1]
    counts = counts[::-1]
    conn.close()

    plt.figure(facecolor='#153152')
    plt.bar(dates, counts, color="#255999")
    plt.tick_params(axis='x', colors='white')
    plt.tick_params(axis='y', colors='white')
    plt.xlabel('Дата', color='#153152')
    plt.ylabel('Количество обработанных фото', color='#153152')
    plt.title('Статистика использования', color='white')
    imgdata = StringIO()

    plt.savefig(imgdata, format='svg')
    imgdata.seek(0)
    data = imgdata.getvalue()
    return data


def graph_view(request):
    graph_file = generate_graph()
    template = loader.get_template('graph.html')
    context = {'graph_file': graph_file}
    return HttpResponse(template.render(context, request))
