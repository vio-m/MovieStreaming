from django.contrib import admin
from .models import Video, Genre
from embed_video.admin import AdminVideoMixin


class AdminVideo(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(Video, AdminVideo)
admin.site.register(Genre)

