from tabnanny import verbose

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length= 100, verbose_name='Titulo do Evento')
    description = models.TextField(blank=True, null=True)
    date_event = models.DateField(verbose_name='Data do Evento')
    date_creation = models.TimeField(auto_now=True, verbose_name='Criado em')
    local = models.CharField(max_length=255, verbose_name='Local do Evento')
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # se o usuario dor deletado ele vai deletar todos os eventos que ele cadastrou

    class Meta:
        db_table = 'event'


    def get_data_event(self):
        return self.date_event.strftime('%d/%m/%Y %H : %M')

