# Generated by Django 4.2 on 2023-05-07 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="City",
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
                ("name", models.CharField(max_length=100)),
                ("lat", models.FloatField()),
                ("lon", models.FloatField()),
                ("timezone", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="HourlyWeather",
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
                ("dt", models.DateTimeField()),
                ("temp", models.FloatField()),
                ("feels_like", models.FloatField()),
                ("pressure", models.FloatField()),
                ("humidity", models.FloatField()),
                ("clouds", models.FloatField()),
                ("visibility", models.FloatField()),
                ("wind_speed", models.FloatField()),
                ("wind_gust", models.FloatField(null=True)),
                ("wind_deg", models.FloatField()),
                ("rain_1h", models.FloatField(null=True)),
                ("snow_1h", models.FloatField(null=True)),
                ("weather_id", models.IntegerField()),
                ("weather_main", models.CharField(max_length=100)),
                ("weather_description", models.CharField(max_length=100)),
                ("weather_icon", models.CharField(max_length=50)),
                ("pop", models.FloatField()),
                (
                    "city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="wheater.city"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="DailyWeather",
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
                ("dt", models.DateTimeField()),
                ("temp", models.FloatField()),
                ("feels_like", models.FloatField()),
                ("pressure", models.FloatField()),
                ("humidity", models.FloatField()),
                ("clouds", models.FloatField()),
                ("visibility", models.FloatField()),
                ("wind_speed", models.FloatField()),
                ("wind_gust", models.FloatField(null=True)),
                ("wind_deg", models.FloatField()),
                ("rain_1h", models.FloatField(null=True)),
                ("snow_1h", models.FloatField(null=True)),
                ("weather_id", models.IntegerField()),
                ("weather_main", models.CharField(max_length=100)),
                ("weather_description", models.CharField(max_length=100)),
                ("weather_icon", models.CharField(max_length=50)),
                ("sunrise", models.DateTimeField()),
                ("sunset", models.DateTimeField()),
                ("moonrise", models.DateTimeField()),
                ("moonset", models.DateTimeField()),
                ("moon_phase", models.FloatField()),
                ("temp_morn", models.FloatField()),
                ("temp_day", models.FloatField()),
                ("temp_eve", models.FloatField()),
                ("temp_night", models.FloatField()),
                ("feels_like_morn", models.FloatField()),
                ("feels_like_day", models.FloatField()),
                ("feels_like_eve", models.FloatField()),
                ("feels_like_night", models.FloatField()),
                ("pop", models.FloatField()),
                ("rain", models.FloatField(null=True)),
                ("snow", models.FloatField(null=True)),
                (
                    "city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="wheater.city"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="CurrentWeather",
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
                ("dt", models.DateTimeField()),
                ("temp", models.FloatField()),
                ("feels_like", models.FloatField()),
                ("pressure", models.FloatField()),
                ("humidity", models.FloatField()),
                ("clouds", models.FloatField()),
                ("visibility", models.FloatField()),
                ("wind_speed", models.FloatField()),
                ("wind_gust", models.FloatField(null=True)),
                ("wind_deg", models.FloatField()),
                ("rain_1h", models.FloatField(null=True)),
                ("snow_1h", models.FloatField(null=True)),
                ("weather_id", models.IntegerField()),
                ("weather_main", models.CharField(max_length=100)),
                ("weather_description", models.CharField(max_length=100)),
                ("weather_icon", models.CharField(max_length=50)),
                (
                    "city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="wheater.city"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
