# Generated by Django 3.1.4 on 2021-02-06 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0011_remove_account_currentbalance'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='currentBalance',
            field=models.IntegerField(default=True, null=True),
        ),
    ]
