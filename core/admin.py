from django.contrib import admin
from .models import CustomUser,Profile,Movie,Video
from django.contrib import admin
from .models import Music,Album


# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Profile)
admin.site.register(Movie)
admin.site.register(Video)


admin.site.register(Music)
admin.site.register(Album)