# Generated by Django 3.1.2 on 2020-10-28 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20201026_1844'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-datetime', 'title')},
        ),
    ]