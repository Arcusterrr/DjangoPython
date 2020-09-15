import datetime
from django.db import models

from django.utils import timezone

class Item(models.Model):
    title = models.CharField('Название товара', max_length = 200)
    description = models.TextField('Описание товара')
    pub_date = models.DateField('Дата публикации')
    
    def __str__(self):
        return self.title
        
    def recently_published(self):
        print(datetime.timedelta(days=7))
        print(timezone.now())
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))
    
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Comment(models.Model):
    item = models.ForeignKey(Item, on_delete = models.CASCADE)
    author_name = models.CharField('Имя автора', max_length=50)
    text = models.TextField('Текст комментария')

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
    