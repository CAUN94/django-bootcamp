# Generated by Django 3.1.5 on 2021-01-18 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_wizard'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Wizard',
            new_name='Students',
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
        migrations.RenameField(
            model_name='students',
            old_name='house',
            new_name='clases',
        ),
        migrations.RenameField(
            model_name='students',
            old_name='pet',
            new_name='medals',
        ),
    ]