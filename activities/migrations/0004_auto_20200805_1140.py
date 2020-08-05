# Generated by Django 3.1 on 2020-08-05 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0003_auto_20200804_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='name',
            field=models.CharField(choices=[(None, '--Please choose--'), ('ft', 'Full-time'), ('pt', 'Part-time'), ('contract', 'Contract work')], max_length=10),
        ),
    ]
