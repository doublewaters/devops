# Generated by Django 2.2.3 on 2019-07-29 14:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('webssh', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='terminallog',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='会话开始时间'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='terminallog',
            name='res',
            field=models.TextField(default='未记录', verbose_name='结果详情'),
        ),
    ]