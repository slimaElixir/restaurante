# Generated by Django 4.2.1 on 2023-06-22 10:55

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MenuModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("active", models.BooleanField(default=True, verbose_name="Activo")),
                (
                    "delected",
                    models.BooleanField(default=False, verbose_name="Apagado"),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Nome")),
                (
                    "sort_order",
                    models.IntegerField(db_index=True, editable=False, null=True),
                ),
                ("app_name", models.CharField(max_length=100)),
                ("icon", models.CharField(max_length=50)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="VersionModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("active", models.BooleanField(default=True, verbose_name="Activo")),
                (
                    "delected",
                    models.BooleanField(default=False, verbose_name="Apagado"),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Nome")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "version",
                    models.CharField(editable=False, max_length=100, unique=True),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ReleaseNoteModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("active", models.BooleanField(default=True, verbose_name="Activo")),
                (
                    "delected",
                    models.BooleanField(default=False, verbose_name="Apagado"),
                ),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Descricao"),
                ),
                ("note_type", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "version",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="release_notes",
                        to="core_app.versionmodel",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="MenuItemModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("active", models.BooleanField(default=True, verbose_name="Activo")),
                (
                    "delected",
                    models.BooleanField(default=False, verbose_name="Apagado"),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Nome")),
                (
                    "sort_order",
                    models.IntegerField(db_index=True, editable=False, null=True),
                ),
                ("url_name", models.CharField(blank=True, max_length=100, null=True)),
                ("lft", models.PositiveIntegerField(editable=False)),
                ("rght", models.PositiveIntegerField(editable=False)),
                ("tree_id", models.PositiveIntegerField(db_index=True, editable=False)),
                ("level", models.PositiveIntegerField(editable=False)),
                (
                    "menu",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="core_app.menumodel",
                    ),
                ),
                (
                    "parent",
                    mptt.fields.TreeForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="children",
                        to="core_app.menuitemmodel",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]