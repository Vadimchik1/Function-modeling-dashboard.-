# Generated by Django 3.2.6 on 2021-08-26 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='function',
            name='picture',
            field=models.ImageField(null=True, upload_to='pictures/%Y/%m/%d/'),
        ),
    ]
