from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.CodingChallenge)
admin.site.register(models.Badge)
admin.site.register(models.UserBadge)