from django.urls import path, register_converter
from datetime import datetime

from app.views import file_list, file_content


class DateConverter:
    regex = r'[0-9]{4}-[0-9]{2}-[0-9]{2}'
    format = '%Y-%m-%d'

    def to_python(self, value: str) -> datetime:
        return datetime.strptime(value, self.format)

    def to_url(self, value: datetime) -> str:
        return value.strftime(self.format)


register_converter(DateConverter, 'date')


urlpatterns = [
    # Определите схему урлов с привязкой к отображениям .views.file_list и .views.file_content
    path('', file_list, name='file_list'),
    path('<date:date>/', file_list, name='file_list'),    # задайте необязательный параметр "date"
    path('<path:name>/', file_content, name='file_content'),
]
