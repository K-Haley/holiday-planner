# Generated by Django 2.1.4 on 2018-12-18 23:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
        ('events_app', '0002_auto_20181218_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='foods',
            name='brought_by',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='login_app.Users'),
        ),
    ]