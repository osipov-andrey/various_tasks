from django.conf import settings
from django.db import models


class Issue(models.Model):
    name = models.CharField('Название', max_length=512)
    description = models.TextField('Описание', default='')
    due_date = models.DateField('Выполнить к дате')

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'

    def __str__(self):
        return self.name

    def set_due_date(self, due_date):
        self.due_date = due_date

    def foo(self):
        if settings.DEBUG:
            return self.name
        return 'stub'

    def bar(self):
        if settings.ADMINS_NAME in settings.CUSTOM_LIST:
            return self.name
        return 'stub'
