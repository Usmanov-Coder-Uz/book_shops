from .models import Category,Author,Book

from rest_framework import serializers

class BookSerilaizer(serializers.ModelSerializer):
    category_name = serializers.CharField(source = 'category.name')

    author_name = serializers.CharField(source = 'author.full_name')

    
    class Meta:
        model = Book
        fields = ('id','author_name','category_name','name','category','author','description','photo','isbn','file','audio','downloads_count',)

class CategorySerilaizer(serializers.ModelSerializer):
    book_category = BookSerilaizer(many =True,read_only = True)
    class Meta:
        model = Category
        fields = ('name','id','status','book_category')
class AuthorSerilaizer(serializers.ModelSerializer):
    book_author = BookSerilaizer(many = True, read_only =  True)
    class Meta:
        model = Author
        fields = ('full_name','id','status','book_author')



