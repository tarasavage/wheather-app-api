from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100)
    lat = models.FloatField()
    lon = models.FloatField()
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Weather(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    dt = models.DateTimeField()
    temp = models.FloatField()
    feels_like = models.FloatField()
    pressure = models.FloatField()
    humidity = models.FloatField()
    clouds = models.FloatField()
    visibility = models.FloatField()
    wind_speed = models.FloatField()
    wind_gust = models.FloatField(null=True)
    wind_deg = models.FloatField()
    rain_1h = models.FloatField(null=True)
    snow_1h = models.FloatField(null=True)
    weather_id = models.IntegerField()
    weather_main = models.CharField(max_length=100)  # "Rain"
    weather_description = models.CharField(max_length=100)  # "light rain"
    weather_icon = models.CharField(max_length=50)  # "10n"

    class Meta:
        abstract = True


class CurrentWeather(Weather):
    def __str__(self):
        return f"Current weather for {self.city.name} at {self.dt}"


class HourlyWeather(Weather):
    pop = models.FloatField()

    def __str__(self):
        return f"Hourly weather for {self.city.name} at {self.dt}"


class DailyWeather(Weather):
    sunrise = models.DateTimeField()
    sunset = models.DateTimeField()
    moonrise = models.DateTimeField()
    moonset = models.DateTimeField()
    moon_phase = models.FloatField()
    temp_morn = models.FloatField()
    temp_day = models.FloatField()
    temp_eve = models.FloatField()
    temp_night = models.FloatField()
    feels_like_morn = models.FloatField()
    feels_like_day = models.FloatField()
    feels_like_eve = models.FloatField()
    feels_like_night = models.FloatField()
    pop = models.FloatField()
    rain = models.FloatField(null=True)
    snow = models.FloatField(null=True)

    def __str__(self):
        return f"Daily weather for {self.city.name} on {self.dt}"
