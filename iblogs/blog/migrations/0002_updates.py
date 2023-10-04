# Generated by Django 4.2.1 on 2023-09-29 14:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Updates",
            fields=[
                ("update_id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("url", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="updates/")),
                ("add_date", models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
