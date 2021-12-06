# Generated by Django 3.2.9 on 2021-12-06 07:06

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0002_alter_music_album_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='album_name',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='artist', chained_model_field='related_artist', on_delete=django.db.models.deletion.CASCADE, to='rest.album'),
        ),
    ]