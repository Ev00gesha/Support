from django.db import models
from django.urls import reverse

# Create your models here.

class Types_request(models.Model):
    type_req = models.CharField(max_length=50)
    def __str__(self):
        return self.type_req

class Resuests(models.Model):
    user = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    type_request = models.ForeignKey(
        Types_request,
        on_delete=models.CASCADE, verbose_name='Тип заявки'
    )
    body = models.TextField('Заявка')
    date = models.DateField(verbose_name='Дата', auto_now=True)
    def __str__(self):
        return f"{self.login} {self.body[:20]}"

    def get_absolute_url(self):
        return reverse('my_account')

    class Meta:
        verbose_name_plural = 'Заявки'


class Answer(models.Model):
    request_id = models.ForeignKey(Resuests, on_delete=models.CASCADE)
    answer = models.TextField(verbose_name='Ответ')
    
    def get_absolute_url(self):
        return reverse('my_account')
