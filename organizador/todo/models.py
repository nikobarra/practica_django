from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    priority = models.IntegerField(default = 3)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
