from django.db import models

class Lesson(models.Model):
    dars_n = models.CharField(max_length=100)

    def __str__(self):
        return self.dars_n


class Salom(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Jamoa(models.Model):
    img = models.ImageField(upload_to='img/')  # Bu joyda Pillow kerak bo'ladi
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name