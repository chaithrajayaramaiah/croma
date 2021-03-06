# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-21 07:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('godown_master', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('master', models.IntegerField(blank=True, default=0, null=True)),
                ('group', models.IntegerField(blank=True, default=0, null=True)),
                ('full_path', models.CharField(default='TOP', max_length=200)),
                ('nodes', models.IntegerField(blank=True, default=0, null=True)),
                ('category', models.CharField(blank=True, default='COMPANY', max_length=50, null=True)),
                ('total', models.IntegerField(blank=True, default=0, null=True)),
                ('use_date', models.DateField(blank=True, null=True)),
                ('use_time', models.TimeField(blank=True, null=True)),
                ('user_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Chain',
                'verbose_name_plural': 'Chains',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('short_name', models.CharField(blank=True, max_length=80, null=True)),
                ('add1', models.CharField(blank=True, max_length=150, null=True)),
                ('add2', models.CharField(blank=True, max_length=150, null=True)),
                ('add3', models.CharField(blank=True, max_length=150, null=True)),
                ('city', models.CharField(blank=True, max_length=60, null=True)),
                ('phone1', models.CharField(blank=True, max_length=12, null=True)),
                ('phone2', models.CharField(blank=True, max_length=12, null=True)),
                ('ptax', models.IntegerField(blank=True, default=5, null=True)),
                ('use_date', models.DateField(blank=True, null=True)),
                ('use_time', models.TimeField(blank=True, null=True)),
                ('stax', models.IntegerField(blank=True, default=3, null=True)),
                ('chain_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='company_master.Chain')),
                ('godown_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='godown_master.Godown')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('person', models.CharField(blank=True, max_length=150, null=True)),
                ('add1', models.CharField(blank=True, max_length=150, null=True)),
                ('add2', models.CharField(blank=True, max_length=150, null=True)),
                ('add3', models.CharField(blank=True, max_length=150, null=True)),
                ('city', models.CharField(blank=True, max_length=60, null=True)),
                ('phone1', models.CharField(blank=True, max_length=12, null=True)),
                ('phone2', models.CharField(blank=True, max_length=12, null=True)),
                ('lst_num', models.CharField(blank=True, max_length=12, null=True)),
                ('cst_num', models.CharField(blank=True, max_length=12, null=True)),
                ('drug_license1', models.CharField(blank=True, max_length=40, null=True)),
                ('drug_license2', models.CharField(blank=True, max_length=40, null=True)),
                ('tin_no', models.CharField(blank=True, max_length=40, null=True)),
                ('pin_no', models.CharField(blank=True, max_length=40, null=True)),
                ('c_days', models.IntegerField(blank=True, default=0, null=True)),
                ('c_limit', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('use_date', models.DateField(blank=True, null=True)),
                ('less_by', models.IntegerField(blank=True, default=0, null=True)),
                ('use_time', models.TimeField(blank=True, null=True)),
                ('identity', models.CharField(blank=True, max_length=30, null=True)),
                ('account_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.Accounts')),
                ('head_id', models.ForeignKey(default=22, on_delete=django.db.models.deletion.CASCADE, to='accounts.Head')),
                ('user_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Supplier',
                'verbose_name_plural': 'Suppliers',
            },
        ),
        migrations.AddField(
            model_name='company',
            name='supp_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='company_master.Supplier'),
        ),
        migrations.AddField(
            model_name='company',
            name='user_id',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
