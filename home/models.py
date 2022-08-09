# from django.db import models
#
# # Create your models here.
#
#
# #
# # class ElasticDemo(models.Model):
# #
# #     title = models.CharField(max_length=100)
# #     content = models.TextField()
#
# class ElasticDemo2(models.Model):
#     link=models.CharField(max_length=300)
#     date=models.CharField(max_length=50)
#     title = models.CharField(max_length=400)
#     content = models.TextField()
#
#     # def __str__(self):
#     #     return '%s' % (self.title)
#







from django.db import models

# Create your models here.



class ElasticDemo(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
