from django.contrib import admin
from django.utils.safestring import mark_safe
from profiles.models import Profile

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "nickname"]
    readonly_fields = [
        "get_image", "slug"
    ]

    def get_image(self, obj):
        return mark_safe(f'<img scr>={obj.avatar.url} width="110" height="100">')

    get_image.short_description = "Avatar"
