# Generated by Django 4.2.3 on 2023-08-10 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock_management', '0006_alter_item_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventorylocation',
            old_name='user',
            new_name='user_id',
        ),
    ]
