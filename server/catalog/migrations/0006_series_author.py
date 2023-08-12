# Generated by Django 4.2.4 on 2023-08-12 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0005_series_total_books"),
    ]

    operations = [
        migrations.AddField(
            model_name="series",
            name="author",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="catalog.author",
            ),
            preserve_default=False,
        ),
    ]
