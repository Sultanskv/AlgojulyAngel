# Generated by Django 5.0.6 on 2024-08-12 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_ind_clientdt_paid_paln_alter_ind_clientdt_clint_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.AlterField(
            model_name='ind_clientdt',
            name='clint_id',
            field=models.CharField(default='002f5b3b', max_length=8, unique=True),
        ),
    ]
