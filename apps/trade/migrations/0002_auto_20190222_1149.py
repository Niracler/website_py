# Generated by Django 2.1.7 on 2019-02-22 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordergoods',
            old_name='goods_num',
            new_name='nums',
        ),
    ]
