# Generated by Django 4.0.5 on 2022-07-05 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('canvas', '0004_rename_content_id_result_content_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Result',
        ),
    ]
