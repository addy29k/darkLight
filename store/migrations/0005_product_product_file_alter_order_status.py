# Generated by Django 4.2.7 on 2023-12-01 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20210529_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_file',
            field=models.FileField(blank=True, null=True, upload_to='product'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Packed', 'Packed'), ('On The Way', 'On The Way'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default='Pending', max_length=50),
        ),
    ]
