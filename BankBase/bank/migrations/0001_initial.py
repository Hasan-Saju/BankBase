# Generated by Django 3.1.4 on 2021-02-06 19:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('account_name', models.CharField(default='Blank. Set Account Name', max_length=30)),
                ('dob', models.DateField(blank=True, null=True)),
                ('password', models.CharField(max_length=15)),
                ('currentBalance', models.IntegerField(default=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AccountType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
                ('InterestRate', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=30)),
                ('managerName', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sourceAccount', models.BigIntegerField(blank=True, null=True)),
                ('destAccount', models.BigIntegerField(blank=True, null=True)),
                ('amount', models.IntegerField()),
                ('timestamp', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LinkedIn_ID', models.URLField(blank=True)),
                ('Employee_Photo', models.ImageField(blank=True, upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_amount', models.IntegerField()),
                ('interestRate', models.FloatField()),
                ('loanPeriod', models.DateField()),
                ('remainingTerms', models.IntegerField()),
                ('accountNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.account')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('contactNo', models.BigIntegerField()),
                ('address', models.CharField(max_length=40)),
                ('accountNum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.account')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='account_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.accounttype'),
        ),
        migrations.AddField(
            model_name='account',
            name='branch_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.branch'),
        ),
    ]
