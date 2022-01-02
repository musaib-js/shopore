# Generated by Django 3.2.4 on 2022-01-02 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('M', 'Mobile'), ('L', 'Laptop'), ('EL', 'Electronics'), ('HE', 'Hearing and Music'), ('WA', 'Watches'), ('TW', 'Top Wear'), ('BW', 'Bottom Wear'), ('BP', 'Beauty Products'), ('MW', 'Mens Footwear'), ('LW', 'Ladies Footwear'), ('KW', 'Kids Wear'), ('KC', 'Knitted Clothes'), ('FR', 'Frozen and Chilled'), ('B', 'Bakery'), ('CA', 'Car Accessories'), ('RF', 'Restaurant Food'), ('GR', 'Groceries'), ('BK', 'Bakeries'), ('RF', 'Restaurant Food'), ('KS', 'Kashmiri Spices')], max_length=2),
        ),
    ]