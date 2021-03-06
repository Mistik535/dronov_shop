from django.contrib import admin

from .models import Bb
from .models import Rubric

class Bdadmin(admin.ModelAdmin):
    list_display = ("title", "content", "price", "published", "rubric")
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')


admin.site.register(Bb, Bdadmin)
admin.site.register(Rubric)
