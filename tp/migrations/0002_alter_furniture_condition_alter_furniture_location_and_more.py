# Generated by Django 4.1.2 on 2022-10-21 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='furniture',
            name='condition',
            field=models.CharField(choices=[('used', 'used'), ('new', 'new'), ('bad', 'bad'), ('broken', 'broken')], default='new', max_length=10),
        ),
        migrations.AlterField(
            model_name='furniture',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='furniture', to='tp.shop'),
        ),
        migrations.AlterField(
            model_name='furniture',
            name='status',
            field=models.CharField(choices=[('sold', 'Sold'), ('available', 'Available')], max_length=10),
        ),
        migrations.AlterField(
            model_name='shop',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shops', to='tp.shopowner'),
        ),
    ]
