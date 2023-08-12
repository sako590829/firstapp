# Generated by Django 4.2.1 on 2023-08-06 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_published_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='num',
        ),
        migrations.AddField(
            model_name='post',
            name='serial_number',
            field=models.PositiveIntegerField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
