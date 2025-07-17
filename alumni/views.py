from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from django.contrib.auth.models import User
from .models import Alumni
from django.contrib.auth.models import User
from .models import Event, Alumni, GalleryImage, LibraryDocument, Testimonial
from .serializers import (
    AlumniSerializer,
    EventSerializer,
    AlumniSerializer,
    GallerySerializer,
    LibrarySerializer,
    TestimonialSerializer
)

from django.contrib.auth.models import User

from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .serializers import AlumniSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def register_alumnus(request):
    serializer = AlumniSerializer(data=request.data)
    if serializer.is_valid():
        # Create user first
        
        user = User.objects.create_user(
            username=request.data['email'],
            email=request.data['email'],
            password=request.data['password']
        )

        # Save alumni and link to user
        alumni = serializer.save()
        alumni.user = user
        alumni.save()

        return Response({"message": "Alumnus registered!"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_profile(request):
    user = request.user
    alumni_profile = Alumni.objects.filter(user=user).first()

    user.username = request.data.get('username', user.username)
    user.email = request.data.get('email', user.email)
    user.save()

    if alumni_profile:
        alumni_profile.phone = request.data.get('phone', alumni_profile.phone)
        alumni_profile.kcse_year = request.data.get('kcse_year', alumni_profile.kcse_year)
        alumni_profile.save()

    return Response({"message": "Profile updated successfully"} )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request):
    user = request.user
    current = request.data.get('current_password')
    new = request.data.get('new_password')

    if not user.check_password(current):
        return Response({'error': 'Current password is incorrect'}, status=400)

    user.set_password(new)
    user.save()
    return Response({'message': 'Password updated successfully'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile_view(request):
    user = request.user
    return Response({
        'username': user.username,
        'email': user.email,
        'id': user.id,
        
    })


class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all().order_by('-created_at')
    serializer_class = TestimonialSerializer
    permission_classes = [permissions.AllowAny]


class LibraryViewSet(viewsets.ModelViewSet):
    queryset = LibraryDocument.objects.all().order_by('-uploaded_at')
    serializer_class = LibrarySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('-date')
    serializer_class = EventSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AlumniViewSet(viewsets.ModelViewSet):
    queryset = Alumni.objects.all()
    serializer_class = AlumniSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GalleryViewSet(viewsets.ModelViewSet):
    queryset = GalleryImage.objects.all()
    serializer_class = GallerySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


