from django.db import models


class Issue(models.Model):

    name = models.CharField('Название', max_length=512)
    description = models.TextField('Описание', default='')
    due_date = models.DateField('Выполнить к дате')

    class Meta:
        verbose_name = "Заметка"
        verbose_name_plural = "Заметки"
