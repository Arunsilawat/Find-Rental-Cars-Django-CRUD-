# Generated by Django 5.1.2 on 2024-10-13 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_book_data_address_remove_book_data_amount_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userdata1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=25)),
            ],
        ),
        migrations.DeleteModel(
            name='Book_data',
        ),
    ]
