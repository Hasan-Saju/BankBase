# Generated by Django 3.1.4 on 2020-12-17 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0003_auto_20201217_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='account_name',
            field=models.CharField(default='Blank. Set Account Name', max_length=30),
        ),
        migrations.AlterField(
            model_name='account',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]