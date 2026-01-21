from django.db import models
from django.conf import settings

class Note(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField() 
    
    COLOR_CHOICES = [
        ('blue', 'Blue'),
        ('yellow', 'Yellow'),
        ('green', 'Green'),
        ('red', 'Red'),
        ('purple', 'Purple'),
    ]
    color = models.CharField(max_length=10, choices=COLOR_CHOICES, default='blue')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title