# Generated by Django 4.0.3 on 2022-03-21 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoods', '0002_alter_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
