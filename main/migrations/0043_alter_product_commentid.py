# Generated by Django 4.1 on 2022-08-17 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0042_alter_sabad_t_comment_product_commentid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='commentID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.comment'),
        ),
    ]