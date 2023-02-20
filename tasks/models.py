from django.db import models
from django.conf import settings 
from django.utils import timezone
from django.core.exceptions import ValidationError


class Task(models.Model):

    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(
        'Título', max_length=150, blank=False, null=False,
    )
    description = models.TextField('Descrição')
    creation_date = models.DateTimeField('Data de criação', auto_now_add=True)
    start_date_task = models.DateTimeField('Data de início da tarefa')
    deadline_date = models.DateTimeField('Data prazo')
    date_conclusion = models.DateTimeField('Data de conclusão', auto_now=True)
    startup_date = models.DateTimeField('Data de inicialização', null=True)
    status = models.BooleanField('Status', default=False)
    punctuality = models.BooleanField('Pontualidade', default=False)
    start_task = models.BooleanField('Iniciar tarefa', default=False)

    def __str__(self) -> str:
        return self.title
    