from django.contrib import admin  # noqa
from core import models

# Register your models here.


admin.site.register(models.User)
admin.site.register(models.Portfolio)
admin.site.register(models.Funds)
