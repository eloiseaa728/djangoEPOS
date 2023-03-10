# Generated by Django 4.1.5 on 2023-01-20 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderID', models.BigIntegerField()),
                ('isSettled', models.BooleanField()),
                ('isSale', models.BooleanField()),
                ('orderTime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EAN', models.BigIntegerField()),
                ('description', models.CharField(max_length=500)),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='vat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vatCode', models.BigIntegerField()),
                ('vat', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('percentageModifier', models.FloatField()),
                ('EAN', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='epos.product')),
                ('orderID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='epos.order')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='vatCode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='epos.vat'),
        ),
        migrations.CreateModel(
            name='priceHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startDate', models.DateTimeField()),
                ('endDate', models.DateTimeField(blank=True)),
                ('net', models.FloatField()),
                ('gross', models.FloatField()),
                ('description', models.CharField(max_length=500)),
                ('EAN', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='epos.product')),
            ],
        ),
    ]
