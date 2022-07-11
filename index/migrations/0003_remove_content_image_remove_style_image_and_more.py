# Generated by Django 4.0.5 on 2022-07-05 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_alter_content_image_alter_style_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='image',
        ),
        migrations.RemoveField(
            model_name='style',
            name='image',
        ),
        migrations.AddField(
            model_name='content',
            name='content-image',
            field=models.FileField(max_length=255, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='style',
            name='style-image',
            field=models.FileField(max_length=255, null=True, upload_to='images/'),
        ),
    ]