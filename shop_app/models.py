from django.db import models

# Create your models here.
class Items(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    img = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'items'