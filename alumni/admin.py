from django.contrib import admin
from .models import Event, Alumni, GalleryImage
from .models import LibraryDocument
from .models import Testimonial


# Customize admin site headers
admin.site.site_header = "Paul Boit Alumni Admin"
admin.site.site_title = "Paul Boit Alumni Admin Portal"
admin.site.index_title = "Welcome to Paul Boit Alumni Admin"

admin.site.register(Testimonial)
admin.site.register(LibraryDocument)
admin.site.register(Event)
admin.site.register(Alumni)
admin.site.register(GalleryImage)
