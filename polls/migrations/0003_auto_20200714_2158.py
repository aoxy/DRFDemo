# Generated by Django 3.0.8 on 2020-07-14 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20200714_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Question'),
        ),
    ]