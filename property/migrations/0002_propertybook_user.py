# Generated by Django 4.0.3 on 2022-03-15 18:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertybook',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='book_owner', to=settings.AUTH_USER_MODEL, verbose_name='user'),
            preserve_default=False,
        ),
    ]
