from django.contrib import admin

from .models import Planet, Filmmaking, Movie, Character


class FilmmakingAdmin(admin.ModelAdmin):
    list_display=['first_name', 'last_name', 'get_type_of_filmmaker_display']

admin.site.register(Filmmaking, FilmmakingAdmin)
admin.site.register(Planet)
admin.site.register(Movie)
admin.site.register(Character)