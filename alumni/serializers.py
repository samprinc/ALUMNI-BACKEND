from rest_framework import serializers
from .models import Alumni
from rest_framework import serializers
from .models import Event, Alumni, GalleryImage
from django.contrib.auth.models import User
from .models import LibraryDocument
from .models import Testimonial


class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryDocument
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

from rest_framework import serializers
from .models import Alumni
from django.contrib.auth.hashers import make_password

class AlumniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumni
        fields = [
            'full_name', 'email', 'phone', 'admission_number',
            'kcse_year', 'course', 'graduation_year', 'password'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])  # hash it
        return super().create(validated_data)


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'
