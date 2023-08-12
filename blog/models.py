from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    serial_number = models.AutoField(primary_key=True, editable=False)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)
    img = models.ImageField(upload_to='post_images/', blank=True, null=True)  # ブランクとヌルを設定


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.title} {self.img}"
    
    def has_image(self):
        return self.img is not None
    

