from django.contrib import admin
from .models import create_blog, resources

# Register your models here.
admin.site.register(create_blog)
admin.site.register(resources)
