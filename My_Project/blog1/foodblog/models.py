from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to="food_blog/")
    created_at = models.DateTimeField(auto_now_add=True)
   

    def __str__(self):
        return self.title