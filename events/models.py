from django.db import models

# Create your models here.
class Event(models.Model):
    # Fields from Events table
    id = models.BigAutoField(primary_key=True)
    event_name = models.CharField(max_length=255)
    event_description = models.TextField(null=True)

    class Meta:
        db_table = 'events'
        verbose_name = ("event")
        verbose_name_plural = ("events")

    def __str__(self):
        return (f"{self.event_name}"
                f"{self.id}"
                f"{self.event_description}")
