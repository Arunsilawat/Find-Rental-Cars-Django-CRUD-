# Generated by Django 5.1.2 on 2024-10-13 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_delete_book_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('carnm', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
                ('address', models.TextField()),
                ('pick', models.CharField(max_length=50)),
                ('drop', models.CharField(max_length=50)),
                ('feedback', models.TextField()),
            ],
        ),
    ]
