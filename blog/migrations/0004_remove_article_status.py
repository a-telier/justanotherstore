# Generated by Django 3.1.2 on 2021-01-31 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_article_banner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='status',
        ),
    ]
