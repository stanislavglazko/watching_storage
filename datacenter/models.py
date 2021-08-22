from django.db import models
from django.utils.timezone import localtime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= 'leaved at ' + str(self.leaved_at) if self.leaved_at else 'not leaved'
        )
    
    def get_duration(self):
        entered_at = localtime(self.entered_at)
        leaved_at = localtime(self.leaved_at)
        time_delta = leaved_at - entered_at
        seconds = time_delta.total_seconds()
        return seconds
    
    def format_duration(self):
        seconds = self.get_duration()
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        seconds = int((seconds % 3600) % 60)
        return f'{hours}ч {minutes}мин {seconds}сек'
    
    def is_visit_long(self, too_long_inside=60):
        seconds = self.get_duration()
        minutes = seconds // 60
        return minutes > too_long_inside
