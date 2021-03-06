# Generated by Django 4.0.4 on 2022-04-19 16:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Timer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('webhook_url', models.CharField(max_length=60)),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('duration', models.IntegerField()),
                ('status', models.TextField(choices=[('Running', 'Running'), ('Paused', 'Paused'), ('Finished', 'Finished')], default='Running')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
