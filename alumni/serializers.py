from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import (
    Alumni, Event, GalleryImage,
    LibraryDocument, Testimonial
)

# ✅ Hash password before saving new alumni
class AlumniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumni
        fields = [
            'full_name', 'email', 'phone', 'admission_number',
            'kcse_year', 'course', 'graduation_year', 'password'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


# ✅ Ensure image field returns full Cloudinary URL
class EventSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Event
        fields = '__all__'


class GallerySerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = GalleryImage
        fields = '__all__'


class LibrarySerializer(serializers.ModelSerializer):
    file = serializers.FileField(use_url=True)

    class Meta:
        model = LibraryDocument
        fields = '__all__'


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'


# ✅ Secure user creation (if used)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
