# Generated by Django 4.1.7 on 2023-03-29 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_blogs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogs',
            old_name='email',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='blogs',
            old_name='name',
            new_name='username',
        ),
    ]