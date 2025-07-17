from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    profile_view,
    update_profile,
    change_password,
    TestimonialViewSet,
    LibraryViewSet,
    EventViewSet,
    AlumniViewSet,
    GalleryViewSet,
    register_alumnus,
)

router = DefaultRouter()
router.register(r'testimonials', TestimonialViewSet)
router.register(r'library', LibraryViewSet)
router.register(r'events', EventViewSet)
router.register(r'alumni', AlumniViewSet)
router.register(r'gallery', GalleryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('profile/', profile_view),  # GET
    path('profile/update/', update_profile),  # PATCH
    path('profile/change-password/', change_password),  # POST
    path('register/', register_alumnus),  # POST
]
