from rest_framework import serializers
from .models import Post
from django import forms

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title',
            'description',
            'owner'
        )

# normal method without serializer
# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         field = (
#             'title', 'description'
#         )