from django.db import models
# Create your models here.
class Category(models.Model):
    ACTION = 'ACT'
    ROMANTIC = 'ROM'
    HORROR = 'HOR'
    GENRES = [
        (ACTION, 'Action'),
        (ROMANTIC, 'Romantic'),
        (HORROR, 'Horror'),
    ]
    category = models.CharField(max_length=3, choices=GENRES, null=True, default=ACTION)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.category