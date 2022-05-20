# Generated by Django 4.0.4 on 2022-05-18 00:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('weatherapp', '0003_alter_city_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('lat', models.DecimalField(decimal_places=9, max_digits=12)),
                ('lon', models.DecimalField(decimal_places=9, max_digits=12)),
                ('country', models.CharField(max_length=5)),
                ('state', models.CharField(max_length=35)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Locations',
            },
        ),
    ]
