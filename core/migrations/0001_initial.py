# Generated by Django 4.0.3 on 2022-03-03 22:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProxyLists',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('ip_address', models.GenericIPAddressField(null=True)),
                ('port', models.IntegerField(blank=True, null=True)),
                ('protocol', models.CharField(blank=True, max_length=15, null=True)),
                ('anonymity', models.CharField(blank=True, max_length=30, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('region', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('uptime', models.CharField(blank=True, max_length=15, null=True)),
                ('response', models.CharField(blank=True, max_length=15, null=True)),
                ('speed', models.CharField(blank=True, max_length=15, null=True)),
                ('last_checked', models.CharField(blank=True, max_length=30)),
            ],
        ),
    ]