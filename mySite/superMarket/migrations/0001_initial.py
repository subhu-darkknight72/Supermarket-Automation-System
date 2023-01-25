# Generated by Django 4.0.3 on 2022-03-30 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('p_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('brand', models.CharField(max_length=20)),
                ('p_name', models.CharField(max_length=50)),
                ('cost_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('qty', models.IntegerField(default=0)),
                ('type', models.CharField(choices=[('by_qty', 'by quantity'), ('by_wt', 'by weight')], default='by_qty', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='transaction',
            fields=[
                ('t_id', models.AutoField(primary_key=True, serialize=False)),
                ('t_date', models.CharField(default='2022/04/03', max_length=10, null=True)),
                ('total_cost', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('profit', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('tax', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('customer_id', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='sold_product',
            fields=[
                ('ps_id', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('tran_id', models.IntegerField(default=0)),
                ('t_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('quantity', models.IntegerField(default=1)),
                ('unit_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('item_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('tax', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('net_cost', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('profit', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='superMarket.product')),
            ],
        ),
    ]
