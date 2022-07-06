from django.contrib import admin

from shared import models


to_register = [
    models.Genre,
]

admin.site.register(to_register)
