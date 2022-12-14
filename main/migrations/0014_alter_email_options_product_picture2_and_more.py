# Generated by Django 4.1 on 2022-08-05 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_offer_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='email',
            options={},
        ),
        migrations.AddField(
            model_name='product',
            name='picture2',
            field=models.ImageField(default=None, upload_to='ProductImage/picture2', verbose_name='عکس پیش نمایش'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='picture3',
            field=models.ImageField(default=None, upload_to='ProductImage/picture3', verbose_name='عکس جزيیات'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='picture4',
            field=models.ImageField(default=None, upload_to='ProductImage/picture4', verbose_name='عکس جزییات'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='Tpost',
            field=models.IntegerField(default=0, verbose_name='تعداد پست'),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='category', verbose_name='عکس '),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255, verbose_name='اسم '),
        ),
        migrations.AlterField(
            model_name='image_trend_2',
            name='image1',
            field=models.ImageField(upload_to='main/pic/1', verbose_name='عکس اولی'),
        ),
        migrations.AlterField(
            model_name='image_trend_2',
            name='image2',
            field=models.ImageField(upload_to='main/pic/2', verbose_name='عکس دومی'),
        ),
        migrations.AlterField(
            model_name='image_u',
            name='image',
            field=models.ImageField(upload_to='main/u', verbose_name='عکس'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='darsad',
            field=models.IntegerField(verbose_name='درصد تخفیف'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='time',
            field=models.DateTimeField(verbose_name='زمان تخفیف'),
        ),
        migrations.AlterField(
            model_name='product',
            name='buyers',
            field=models.IntegerField(default=0, verbose_name='تعداد فروش'),
        ),
        migrations.AlterField(
            model_name='product',
            name='caption',
            field=models.TextField(verbose_name='معرفی جزیَی'),
        ),
        migrations.AlterField(
            model_name='product',
            name='detail',
            field=models.TextField(verbose_name='معرفی دقیق'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255, verbose_name='عکس محصول'),
        ),
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(upload_to='ProductImage', verbose_name='عکس نمایشی'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(verbose_name='قیمت به تومان'),
        ),
        migrations.AlterField(
            model_name='product',
            name='star',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], verbose_name='امتیاز به ستاره'),
        ),
        migrations.AlterField(
            model_name='product',
            name='view',
            field=models.IntegerField(default=0, verbose_name='تعداد بازدید'),
        ),
        migrations.AlterModelTable(
            name='email',
            table=None,
        ),
    ]
