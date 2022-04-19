from django.utils import timezone
from django.db import models

# Create your models here.


class Timer(models.Model):
    id = models.AutoField(primary_key=True)

    webhook_url = models.CharField(max_length=60)

    start_time = models.DateTimeField(default=timezone.now)
    duration = models.IntegerField()

    class TimerStatus(models.TextChoices):
        RUNNING = 'Running'
        PAUSED = 'Paused'
        FINISHED = 'Finished'

    status = models.TextField(
        choices=TimerStatus.choices, default=TimerStatus.RUNNING)

    created_at = models.DateTimeField(auto_now_add=True)

    def get_remaining(self):
        self.refresh_status()

        if self.status == Timer.TimerStatus.FINISHED:
            return 0
        else:
            elapsed = timezone.now() - self.start_time
            return self.duration - elapsed.seconds * 1000

    def refresh_status(self):
        if self.status == Timer.TimerStatus.RUNNING:
            elapsed = timezone.now() - self.start_time
            if self.duration <= elapsed.seconds * 1000:
                self.status = Timer.TimerStatus.FINISHED
                self.save()

    def pause(self):
        self.refresh_status()

        if self.status == Timer.TimerStatus.RUNNING:
            self.status = Timer.TimerStatus.PAUSED
            elapsed = timezone.now() - self.start_time
            self.duration -= elapsed.seconds * 1000
            self.save()

    def resume(self):
        if self.status == Timer.TimerStatus.PAUSED:
            self.status = Timer.TimerStatus.RUNNING
            self.start_time = timezone.now()
            self.save()
