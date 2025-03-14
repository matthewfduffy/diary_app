from django.db import models
from django.utils import timezone

class Entry(models.Model):
    # Django automatically adds 'id' as a unique primary key
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)


    # by default the string representation of an entry with a PK would be "Entry object (1)"
    # customize this behavior by adding_ _str__() 
    def __str__(self):
        return self.title

    # overrides Django behavior that would display the plural of 'Entry' as 'Entrys'
    class Meta:
        verbose_name_plural = "Entries"
