# Generated by Django 3.0.2 on 2020-01-22 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('naveena', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='naveena',
            options={},
        ),
        migrations.AlterModelManagers(
            name='naveena',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='naveena',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='naveena',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='naveena',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='naveena',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='naveena',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='naveena',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='naveena',
            name='password',
        ),
        migrations.RemoveField(
            model_name='naveena',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='naveena',
            name='username',
        ),
        migrations.AlterField(
            model_name='naveena',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='naveena',
            name='first_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='naveena',
            name='last_name',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]