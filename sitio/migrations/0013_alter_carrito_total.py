# Generated by Django 3.2.4 on 2021-07-06 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0012_auto_20210706_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrito',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
