# Generated by Django 3.2.5 on 2021-07-19 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carusel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carusel_img', models.ImageField(upload_to='sliderimg/', verbose_name='Картинка слайда')),
                ('carusel_text', models.CharField(max_length=250, verbose_name='Текст слайда')),
                ('carusel_title', models.CharField(max_length=250, verbose_name='Заголовок слайда')),
                ('carusel_css', models.CharField(default='-', max_length=250, null=True, verbose_name='CSS класс')),
            ],
            options={
                'verbose_name': 'Слайд',
                'verbose_name_plural': 'Слайды',
            },
        ),
    ]
