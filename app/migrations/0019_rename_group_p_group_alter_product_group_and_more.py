# Generated by Django 4.0.4 on 2022-10-01 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_product_group_alter_product_item_color_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Group',
            new_name='P_Group',
        ),
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='item_color',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='item_size',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='supplier',
            field=models.CharField(max_length=50),
        ),
    ]