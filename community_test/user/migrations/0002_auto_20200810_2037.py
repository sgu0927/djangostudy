# Generated by Django 2.0.13 on 2020-08-10 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '패스트캠퍼스 사용자', 'verbose_name_plural': '패스틐캠퍼스 사용자'},
        ),
        migrations.AddField(
            model_name='user',
            name='useremail',
            field=models.EmailField(default='test@gmail.com', max_length=128, verbose_name='사용자이메일'),
            preserve_default=False,
        ),
    ]
