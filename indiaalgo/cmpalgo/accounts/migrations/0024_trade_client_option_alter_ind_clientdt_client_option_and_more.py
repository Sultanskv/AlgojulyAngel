# Generated by Django 5.0.6 on 2024-08-13 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_ind_clientdt_client_option_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='trade',
            name='client_option',
            field=models.CharField(choices=[('Alpha Wave', 'Alpha Wave'), ('Gamma Gains', 'Gamma Gains'), ('Beta Balance', 'Beta Balance'), ('Demotrade', 'Demotrade')], default='Demotrade', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ind_clientdt',
            name='client_option',
            field=models.CharField(choices=[('Alpha Wave', 'Alpha Wave'), ('Gamma Gains', 'Gamma Gains'), ('Beta Balance', 'Beta Balance'), ('Demotrade', 'Demotrade')], default='Alpha Wave', max_length=20),
        ),
        migrations.AlterField(
            model_name='ind_clientdt',
            name='clint_id',
            field=models.CharField(default='50e3d0b0', max_length=8, unique=True),
        ),
    ]
