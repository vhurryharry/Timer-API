from django.db import models

# Create your models here.


class Timer(models.Model):
    id = models.AutoField(primary_key=True)

    webhook_url = models.CharField(max_length=60)

    start_time = models.DateTimeField()
    duration = models.IntegerField()

    class TimerStatus(models.IntegerChoices):
        RUNNING = 1
        PAUSED = 2
        FINISHED = 3

    status = models.IntegerField(choices=TimerStatus.choices)

    created_at = models.DateTimeField(auto_now_add=True)
