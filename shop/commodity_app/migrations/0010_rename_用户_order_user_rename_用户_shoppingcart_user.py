# Generated by Django 4.2.4 on 2024-04-03 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commodity_app', '0009_rename_user_order_用户'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='用户',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='shoppingcart',
            old_name='用户',
            new_name='user',
        ),
    ]
