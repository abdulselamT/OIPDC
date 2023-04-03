# Generated by Django 4.1.3 on 2023-03-11 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IPDC', '0002_alter_investor_title_domesticrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domesticrequest',
            name='form_of_investment',
            field=models.CharField(choices=[('soleprorietor', 'soleprorietor'), ('PLC', 'PLC'), ('joint-venture', 'joint-venture')], max_length=300),
        ),
        migrations.CreateModel(
            name='FileInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proposal', models.FileField(upload_to='')),
                ('passport', models.FileField(upload_to='')),
                ('memorendum', models.FileField(upload_to='')),
                ('bank_statement', models.FileField(upload_to='')),
                ('id_card', models.FileField(upload_to='')),
                ('power_of_attorney', models.FileField(blank=True, null=True, upload_to='')),
                ('investor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IPDC.investor')),
            ],
        ),
    ]