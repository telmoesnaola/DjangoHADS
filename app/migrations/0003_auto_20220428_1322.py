# Generated by Django 2.2.5 on 2022-04-28 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20220428_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='imagen',
            field=models.ImageField(default='notfound.jpg', upload_to='images/'),
        ),
    ]
