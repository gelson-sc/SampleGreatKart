from django.contrib import admin

from apps.category.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'slug', 'description', 'category_image']
    prepopulated_fields = {'slug': ('category_name',)}


admin.site.register(Category, CategoryAdmin)


