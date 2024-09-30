from django.contrib import admin

from petstagram.photos.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'date_of_publication', 'description', 'get_tagged_animals']

    @staticmethod
    def get_tagged_animals(obj):
        return ', '.join([a.name for a in obj.tagged_pets.all()])
