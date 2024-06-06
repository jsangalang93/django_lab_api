from django.contrib import admin

# Register your models here.
from .models import companies, locations
admin.site.register(companies)
admin.site.register(locations)
