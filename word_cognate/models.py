from django.db import models

# Create your models here.

class Cognates(models.Model):
    english_word = models.CharField(max_length=200)
    language_word = models.CharField(max_length=200)

    def __str__(self):
        return self.english_word


class FalseCognates(models.Model):
    english_word = models.CharField(max_length=200)
    language_word = models.CharField(max_length=200)
    language_definition = models.CharField(max_length=200)

    def __str__(self):
        return self.english_word
