# Generated by Django 3.1.4 on 2020-12-17 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0004_auto_20201217_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='loanPeriod',
            field=models.DateField(),
        ),
    ]
