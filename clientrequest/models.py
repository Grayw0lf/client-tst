from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Responsible(models.Model):
    fio = models.TextField(max_length=255,
                           null=False,
                           blank=False,
                           verbose_name='ФИО')
    position = models.TextField(max_length=255,
                                null=False,
                                blank=False,
                                verbose_name='Должность')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.fio


class Client(models.Model):
    fio = models.TextField(max_length=255,
                           null=False,
                           blank=False,
                           verbose_name='ФИО')
    phone = PhoneNumberField(verbose_name='Телефон')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.fio


class Requisition(models.Model):
    text = models.CharField()
    date = models.DateTimeField(auto_now_add=True)
    responsible = models.ForeignKey(Responsible, on_delete=models.SET_NULL)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return f'Заявка {self.id} - {self.client.fio}'
