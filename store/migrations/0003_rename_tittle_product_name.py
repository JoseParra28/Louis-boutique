# Generated by Django 3.2 on 2023-05-10 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='tittle',
            new_name='name',
        ),
    ]