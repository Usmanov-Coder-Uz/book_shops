from django.contrib import admin
from.models import Category,Author,Book
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    list_filter = ('name','created_at')
    search_fields = ('created_at','name')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name','id','created_at')
    list_filter = ('full_name','created_at')
    search_fields = ('full_name','status','created_at','id')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name','id','isbn','category','author','downloads_count')
    list_filter = ('name','created_at')
    search_fields = ('name','status','created_at','id')











