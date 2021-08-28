
from django.db import models

# Create your models here.
class Carusel(models.Model):
    carusel_img = models.ImageField(upload_to='sliderimg/', verbose_name='Картинка слайда')
    carusel_text = models.CharField(max_length=250, verbose_name='Текст слайда')
    carusel_title = models.CharField(max_length=250, verbose_name='Заголовок слайда')
    carusel_css = models.CharField(max_length=250, null=True, default='-', verbose_name='CSS класс')
    def __str__(self):
        return self.carusel_title
    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'