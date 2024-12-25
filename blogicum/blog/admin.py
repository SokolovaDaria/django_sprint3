from django.contrib import admin

from django.contrib import admin
from .models import Post, Category, Location


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date',
                    'is_published', 'created_at')
    list_filter = ('is_published', 'author', 'category')
    search_fields = ('title', 'text')
    date_hierarchy = 'pub_date'
    ordering = ('-pub_date',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published', 'created_at')
    list_filter = ('is_published',)
    search_fields = ('title', 'description')


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'created_at')
    list_filter = ('is_published',)
    search_fields = ('name',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
