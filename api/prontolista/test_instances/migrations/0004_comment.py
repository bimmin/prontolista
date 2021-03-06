# Generated by Django 2.2.7 on 2019-11-13 07:26

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [("test_instances", "0003_auto_20191113_0104")]

    operations = [
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name="modified"
                    ),
                ),
                ("text", models.TextField(blank=True, null=True)),
                (
                    "test_instance",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="test_instances.TestInstance",
                    ),
                ),
            ],
            options={
                "ordering": ("-modified", "-created"),
                "get_latest_by": "modified",
                "abstract": False,
            },
        )
    ]
