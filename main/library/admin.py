from django.contrib import admin

from .models import Tag, Novel, Manga, Comic, NonFiction

admin.site.register(Tag)
admin.site.register(Novel)
admin.site.register(Manga)
admin.site.register(Comic)
admin.site.register(NonFiction)