# Generated by Django 4.2 on 2023-05-03 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0008_alter_produit_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='img',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]