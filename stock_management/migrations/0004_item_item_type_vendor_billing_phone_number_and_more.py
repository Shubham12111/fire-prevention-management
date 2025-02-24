# Generated by Django 4.2.3 on 2023-08-10 06:54

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock_management', '0003_item_itemimage_remove_productimage_product_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_type',
            field=models.CharField(choices=[('item', 'Item'), ('sor', 'SOR')], default='item', max_length=10),
        ),
        migrations.AddField(
            model_name='vendor',
            name='billing_phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='remarks',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='inventorylocation',
            name='description',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.CreateModel(
            name='VendorContactPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salutation', models.CharField(choices=[('Mr.', 'Mr.'), ('Mrs.', 'Mrs.'), ('Miss', 'Miss')], max_length=10)),
                ('first_name', models.CharField(max_length=127)),
                ('last_name', models.CharField(max_length=127)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=127)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('vendor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock_management.vendor', verbose_name='Vendor')),
            ],
        ),
    ]
