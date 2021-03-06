# Generated by Django 3.1.6 on 2021-02-02 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210202_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='edited_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='edited_articles', to='api.writer'),
        ),
        migrations.AlterField(
            model_name='article',
            name='written_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='api.writer'),
        ),
    ]
