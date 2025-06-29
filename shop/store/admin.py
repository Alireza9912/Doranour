from django.contrib import admin
from .models import Book, Category

@admin.register(Book)
class BookAdmin(admin.ModelAdmin): list_display = ('title', 'author', 'category', 'price')
def get_category(self, obj):
    return obj.category.name
    get_category.short_description = 'Categoty'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin): list_display = ('name',)
# Register your models here.
