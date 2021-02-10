import datetime
import os

from django.shortcuts import render

from .settings import FILES_PATH


def file_list(request, date=None):
    template_name = 'index.html'
    
    context = {
        'files': [],
        'date': date
    }
    files = os.listdir(FILES_PATH)
    for file in files:
        stat = os.stat(FILES_PATH + '/' + file)
        if date is None or datetime.datetime.fromtimestamp(stat.st_ctime).date() == date.date():
            context['files'].append(
                {'name': file,
                 'ctime': datetime.datetime.fromtimestamp(stat.st_ctime),
                 'mtime': datetime.datetime.fromtimestamp(stat.st_mtime)}
            )

    return render(request, template_name, context)


def file_content(request, name):
    with open(FILES_PATH + '/' + name, 'r') as file:
        content = file.read()
    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': content}
    )

