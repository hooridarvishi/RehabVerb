from django.db import models

# Create your models here.
# models.py
from django.db import models

class Card(models.Model):
    title = models.CharField(max_length=100)
    verb = models.CharField(max_length=100)  # فعل سوم شخص
    infinitive = models.TextField()  # مصدر
    image = models.ImageField(upload_to='cards/')
    subject=models.CharField(max_length=320 , blank=True , null=True)
    text_mafool=models.CharField(max_length=100, blank=True , null=True)
    pre_position=models.CharField(max_length=100, blank=True , null=True)
    pre_adverb=models.CharField(max_length=100, blank=True , null=True)
    adverb=models.CharField(max_length=100, blank=True , null=True)

    def __str__(self):
        return self.title

class TextTemplate(models.Model):
    template_text = models.TextField()
    blank1_text = models.CharField(max_length=100, blank=True)
    blank2_text = models.CharField(max_length=100, blank=True)
    blank3_text = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Template #{self.id}"