# Generated by Django 3.1 on 2020-08-05 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0004_auto_20200805_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]