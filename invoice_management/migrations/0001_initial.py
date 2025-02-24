# Generated by Django 4.2.3 on 2024-02-19 06:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('requirement_management', '0045_alter_report_comments'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_json', models.JSONField(verbose_name='Invoice Details')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total Amount')),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('submitted', 'Submitted'), ('send_for_approval', 'Send For Approval'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='draft', max_length=30, verbose_name='Status')),
                ('submitted_at', models.DateTimeField(auto_now_add=True, verbose_name='Submitted At')),
                ('pdf_path', models.CharField(blank=True, max_length=500, null=True, verbose_name='Invoice PDF Path')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL, verbose_name='Customer')),
                ('defects', models.ManyToManyField(to='requirement_management.requirementdefect', verbose_name='Defects')),
                ('quotation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requirement_management.quotation', verbose_name='Quotation')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requirement_management.report', verbose_name='Report')),
                ('requirement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requirement_management.requirement', verbose_name='Requirement')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
            ],
            options={
                'verbose_name': 'Invoice',
                'verbose_name_plural': 'Invoices',
                'ordering': ['-submitted_at'],
            },
        ),
    ]
