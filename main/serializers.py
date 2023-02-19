from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['author', 'name', 'date_created']

class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Author
        fields = ['username', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
        