from django.db import models


class Event(models.Model):
    desc = models.TextField(max_length=2000, blank=False, null=False)
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.timestamp

    def get_absolute_url(self):
        return '/'
