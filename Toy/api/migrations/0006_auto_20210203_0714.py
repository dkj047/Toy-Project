# Generated by Django 3.1.6 on 2021-02-03 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210202_1501'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'permissions': (('can_publish_article', 'Can publish a article'), ('can_edit_article', 'Can edit a article'))},
        ),
    ]