# Generated by Django 2.1.7 on 2019-02-22 02:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodscategorybrand',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='goods.GoodsCategory', verbose_name='商品类目'),
        ),
    ]
