from django.db import models

class Enquiry(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    contact = models.CharField(max_length=11, min_length=11, numeric=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} <{self.email}>"