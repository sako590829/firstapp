# Generated by Django 3.2.20 on 2023-08-09 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_post_published_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, default='noImage.png', upload_to=''),
        ),
    ]
