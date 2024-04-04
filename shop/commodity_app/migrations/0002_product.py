# Generated by Django 4.2.4 on 2024-04-01 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commodity_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('产品名称', models.CharField(max_length=100)),
                ('产品描述', models.TextField()),
                ('产品价格', models.DecimalField(decimal_places=2, max_digits=10)),
                ('产品库存', models.PositiveIntegerField(default=0)),
                ('创建日期', models.DateTimeField(auto_now_add=True)),
                ('产品所属类别', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='commodity_app.category')),
            ],
            options={
                'verbose_name': '产品模型',
                'verbose_name_plural': '产品模型',
                'db_table': 'product',
            },
        ),
    ]
