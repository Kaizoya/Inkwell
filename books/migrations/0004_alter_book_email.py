# Generated by Django 5.0.1 on 2024-04-09 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
