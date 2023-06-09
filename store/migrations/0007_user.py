# Generated by Django 3.1.4 on 2021-06-20 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20210620_0624'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, default='profile1.png', null=True, upload_to='profile_pic')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('Username', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
