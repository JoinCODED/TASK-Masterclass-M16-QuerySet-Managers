from django.contrib import admin

from albums import models


to_register = [
    models.Album,
    models.Song,
]

admin.site.register(to_register)
