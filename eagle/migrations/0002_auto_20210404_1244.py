# Generated by Django 3.0.5 on 2021-04-04 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eagle', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppinglist',
            name='name',
            field=models.CharField(db_index=True, max_length=100),
        ),
    ]
