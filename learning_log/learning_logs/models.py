from django.db import models

class Topic(models.Model):
    """Subject which is studied by the user"""

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns text representation of model."""
        return self.text

class Entry(models.Model):
    """Information studied by the user on a subject"""

    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Returns text representation of model."""
        if len(self.text) > 50:
            return self.text[:50] + "..."
        else:
            return self.text

