# Generated by Django 4.1.5 on 2023-01-24 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sekdilu139', '0010_sosmed_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sosmed',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]