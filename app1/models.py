from django.db import models
import datetime
class BookData(models.Model):
    book_name = models.CharField(max_length=50)
    author_name = models.CharField(max_length=50)
    book_id = models.IntegerField()
    book_price = models.IntegerField()
# Create your models here.
