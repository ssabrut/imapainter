# Generated by Django 4.0.5 on 2022-07-04 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('canvas', '0003_remove_result_image_result_content_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='content_id',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='result',
            old_name='style_id',
            new_name='style',
        ),
    ]
