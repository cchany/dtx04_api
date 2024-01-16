# Generated by Django 4.1 on 2023-12-08 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(help_text='User ID', primary_key=True, serialize=False)),
                ('login_id', models.CharField(max_length=32, unique=True, verbose_name='user 아이디')),
                ('login_pw', models.CharField(max_length=128, verbose_name='user 비밀번호')),
            ],
        ),
        migrations.CreateModel(
            name='User_consultant',
            fields=[
                ('id', models.BigAutoField(help_text='User ID', primary_key=True, serialize=False)),
                ('login_id', models.CharField(max_length=32, unique=True, verbose_name='상담사 아이디')),
                ('login_pw', models.CharField(max_length=128, verbose_name='상담사 비밀번호')),
            ],
        ),
        migrations.CreateModel(
            name='User_Medical',
            fields=[
                ('id', models.BigAutoField(help_text='User ID', primary_key=True, serialize=False)),
                ('login_id', models.CharField(max_length=32, unique=True, verbose_name='의료진 아이디')),
                ('login_pw', models.CharField(max_length=128, verbose_name='의료진 비밀번호')),
            ],
        ),
    ]