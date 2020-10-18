# Generated by Django 3.0.5 on 2020-05-12 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions_api', '0002_auto_20200512_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriptionplan',
            name='feature_ref',
            field=models.CharField(blank=True, help_text='Reference to select list of allowed features for this plan', max_length=100, null=True, unique=True),
        ),
    ]