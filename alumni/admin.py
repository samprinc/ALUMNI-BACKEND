from django.contrib import admin
from .models import Event, Alumni, GalleryImage
from .models import LibraryDocument
from .models import Testimonial


admin.site.register(Testimonial)
admin.site.register(LibraryDocument)
admin.site.register(Event)
admin.site.register(Alumni)
admin.site.register(GalleryImage)
