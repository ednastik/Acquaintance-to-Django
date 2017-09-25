from django.db import models

class Topic(models.Model):
    """Subject which is studied by the user"""

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns text representation of model."""
        return self.text
