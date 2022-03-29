from django.contrib import admin
from .models import Institution, Category
# Register your models here.

@admin.register(Institution)
class Institution(admin.ModelAdmin):
    pass
@admin.register(Category)
class Category(admin.ModelAdmin):
    pass

