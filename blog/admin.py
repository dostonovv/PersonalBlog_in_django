# blog/admin.py
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'views', 'image_preview')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.img:
            return f'<img src="{obj.img.url}" width="150" height="auto" style="border-radius: 8px;" />'
        return 'Rasm yo‘q'

    image_preview.allow_tags = True
    image_preview.short_description = 'Rasm ko‘rinishi'
