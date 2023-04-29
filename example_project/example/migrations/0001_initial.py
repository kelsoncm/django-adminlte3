# Generated by Django 4.0.2 on 2022-02-15 16:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="AllDataTypes",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("small_integer_field", models.SmallIntegerField()),
                ("integer_field", models.IntegerField()),
                ("big_integer_field", models.BigIntegerField()),
                ("positive_small_integer_field", models.PositiveSmallIntegerField()),
                ("positive_integer_field", models.PositiveIntegerField()),
                ("positive_big_integer_field", models.PositiveBigIntegerField()),
                ("decimal_field", models.DecimalField(decimal_places=2, max_digits=10)),
                ("float_field", models.FloatField()),
                ("boolean_field", models.BooleanField()),
                ("desconhecido", models.BooleanField()),
                ("sim", models.BooleanField()),
                ("nao", models.BooleanField()),
                ("char_field", models.CharField(max_length=255)),
                ("text_field", models.TextField()),
                ("slug_field", models.SlugField()),
                ("date_field", models.DateField()),
                ("time", models.TimeField()),
                ("date_time_field", models.DateTimeField()),
                ("duration_field", models.DurationField()),
                ("email_field", models.EmailField(max_length=254)),
                ("generic_ip_address_field", models.GenericIPAddressField()),
                ("url_field", models.URLField()),
                ("json_field", models.JSONField()),
                ("binary_field", models.BinaryField()),
                ("uuid_field", models.UUIDField()),
                ("file_path_field", models.FilePathField()),
                ("file_field", models.FileField(upload_to="")),
                ("image_field", models.ImageField(upload_to="")),
                ("foreign_key_field", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="auth.group")),
                ("many_to_many_field", models.ManyToManyField(to="auth.Permission")),
                (
                    "one_to_one_field",
                    models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
                ),
            ],
        ),
    ]
