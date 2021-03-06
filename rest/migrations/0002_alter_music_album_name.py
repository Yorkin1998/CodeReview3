# Generated by Django 3.2.9 on 2021-12-06 05:32

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='album_name',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='artist', chained_model_field='album_name', on_delete=django.db.models.deletion.CASCADE, to='rest.album'),
        ),
    ]
