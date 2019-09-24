from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class Cost(models.Model):
    title = models.CharField(max_length=100, null=False)
    amount = models.FloatField(null=False)
    date_spent = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        # return f'{self.amount} spent at {self.date_spent} on: "{self.title}"'
        return "{}: {:.2f} spent at {:%Y-%m-%d %H:%M} on: \"{}\"".format(self.author.username, self.amount, self.date_spent, self.title)

    def get_absolute_url(self):
        return reverse('cost-detail', kwargs={'pk': self.pk})