# Generated by Django 4.2.3 on 2024-01-22 08:18

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requirement_management', '0043_alter_sorcategory_options_alter_soritemproxy_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirementdefect',
            name='action',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='requirementdefect',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='requirementdefect',
            name='rectification_description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
