from django.db import models
from .utils import rasm_ulchami
class Lesson(models.Model):
    nomi = models.CharField(max_length=50)

    def __str__(self):
        return self.nomi


class Jamoa(models.Model):
    img = models.ImageField(upload_to="img/", validators=[rasm_ulchami])

    def __str__(self):
        return str(self.img)


class Salom(models.Model):
    ism = models.CharField(max_length=50)

    def __str__(self):
        return self.ism
