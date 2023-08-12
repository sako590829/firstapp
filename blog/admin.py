from django.contrib import admin
from .models import Post
from django.utils.safestring import mark_safe

class PostAdmin(admin.ModelAdmin):
    list_display = ('serial_number', 'text', 'display_image')  

    def display_image(self, obj):    
        if obj.img:
            return mark_safe('<img src="{}" style="width:100px; height:auto;">'.format(obj.img.url))
        return "No Image"
    
admin.site.register(Post, PostAdmin)

