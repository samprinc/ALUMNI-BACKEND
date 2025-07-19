from django.contrib import admin
from .models import Event, Alumni, GalleryImage
from .models import LibraryDocument
from .models import Testimonial


admin.site.site_header = "Paul Boit Alumni Admin"
admin.site.site_title = "Paul Boit Alumni Portal"
admin.site.index_title = "Welcome to Paul Boit Alumni Management"

class CustomAdminSite(admin.AdminSite):
    def each_context(self, request):
        context = super().each_context(request)
        context['custom_admin_css'] = 'alumni/css/admin.css'
        return context

admin.site = CustomAdminSite()


admin.site.register(Testimonial)
admin.site.register(LibraryDocument)
admin.site.register(Event)
admin.site.register(Alumni)
admin.site.register(GalleryImage)
