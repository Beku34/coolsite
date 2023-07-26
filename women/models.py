from django.db import models


# Create your models here.

# class Product(models.Model):
#     model = models.CharField(max_length=255)
#     price = models.FloatField(default=0)
#     color = models.CharField(max_length=255)
#     date_created = models.DateField(auto_now_add=True)
#
#     def __str__(self):
#         return self.model


class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to="images", blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title




    # name = models.CharField(max_length=255)
    # price = models.FloatField(default=0)
    # job = models.CharField(max_length=255)
    # salary = models.FloatField(default=0)



