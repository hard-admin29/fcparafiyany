from django.db import models


class ModelNews(models.Model):
    content: models.FileField = models.FileField(upload_to='media/', default='Default content')
    title: models.CharField = models.CharField("Назва", max_length=250)
    anons: models.CharField = models.CharField("Анонс", max_length=250)
    full_text: models.TextField = models.TextField("Стаття")
    data: models.DateTimeField = models.DateTimeField("Дата публікації")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новина"
        verbose_name_plural = "Новини"

