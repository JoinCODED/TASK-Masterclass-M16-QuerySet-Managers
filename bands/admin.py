from django.contrib import admin

from bands import models


to_register = [
    models.Band,
    models.BandMember,
]

admin.site.register(to_register)
