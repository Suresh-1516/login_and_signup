# Generated by Django 4.1.7 on 2023-06-15 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default=None, max_length=50)),
                ('last_name', models.CharField(default=None, max_length=50)),
                ('addressLine1', models.CharField(default=None, max_length=70)),
                ('city', models.CharField(default=None, max_length=50)),
                ('state', models.CharField(default=None, max_length=50)),
                ('pincode', models.IntegerField(default=None)),
                ('username', models.CharField(default=None, max_length=50)),
                ('user_email', models.EmailField(default=None, max_length=254)),
                ('user_password', models.CharField(default=None, max_length=8)),
                ('user_role', models.CharField(default=None, max_length=50)),
                ('photo', models.ImageField(upload_to='media')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
