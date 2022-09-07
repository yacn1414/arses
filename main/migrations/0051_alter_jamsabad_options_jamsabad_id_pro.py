# Generated by Django 4.1 on 2022-08-22 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0050_alter_sabad_options_remove_sabad_jam_jamsabad'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jamsabad',
            options={'verbose_name': 'jam', 'verbose_name_plural': 'jam sabad'},
        ),
        migrations.AddField(
            model_name='jamsabad',
            name='id_pro',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.product'),
            preserve_default=False,
        ),
    ]
