# Generated by Django 3.0.3 on 2020-02-12 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mysite', '0006_user_epassword'),
    ]

    operations = [
        migrations.CreateModel(
            name='Regis',
            fields=[
                ('rid', models.AutoField(primary_key=True, serialize=False)),
                ('rname', models.CharField(max_length=200)),
                ('remail', models.EmailField(max_length=254)),
                ('rpass', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'registers',
            },
        ),
        migrations.RemoveField(
            model_name='user',
            name='epassword',
        ),
        migrations.AlterModelTable(
            name='user',
            table='register',
        ),
    ]