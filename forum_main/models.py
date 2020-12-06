from django.db import models

# Create your models here.


class Post(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=20000)
    category_choices = [
        ('HOBBIES', 'Hobbies'),
        ('VIDEO', 'Video'),
        ('ARTS', 'Arts'),
        ('GAMING', 'Gaming'),
        ('EXCHANGE', 'Exchange'),
        ('ENTERTAINMENT', 'Entertainment'),
        ('SOCIAL', 'Social'),
        ('RANDOM', 'Random'),
        ('TECH', 'Tech'),
        ('SCIENCE', 'Science'),
        ('Q&As', 'Q&As'),
        ('PETS', 'Pets'),
        ('EDUCATION', 'Education'),
        ('POLITICS', 'Politics'),
    ]
    tags_choices = [
        ('GAMING', 'Gaming'),
        ('NATURE', 'Nature'),
        ('ENTERTAINMENT', 'Entertainment'),
        ('SELFIE', 'Selfie'),
        ('CAMERA', 'Camera'),
        ('USERNAME', 'Username'),
        ('FUNNY', 'Funny'),
        ('PHOTOGRAPHY', 'Photography'),
        ('CLIMBING', 'Climbing'),
        ('ADVENTURE', 'Adventure'),
        ('DREAMS', 'Dreams'),
        ('LIFE', 'Life'),
        ('REASON', 'Reason'),
        ('SOCIAL', 'Social'),
    ]
    category = models.CharField(max_length=15, choices=category_choices, default='Hobbies')
    tags = models.CharField(max_length=15, choices=tags_choices, default='Social')
    is_mature = models.BooleanField(default=False)

