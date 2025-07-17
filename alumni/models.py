from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    location = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="events/", null=True, blank=True)

    def __str__(self):
        return self.title


from django.db import models

class Alumni(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    admission_number = models.CharField(max_length=50)
    kcse_year = models.PositiveIntegerField(default=2020)
    course = models.CharField(max_length=100, blank=True, null=True)
    graduation_year = models.PositiveIntegerField(blank=True, null=True)
    password = models.CharField(max_length=128)  # New field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name




class GalleryImage(models.Model):
    image = models.ImageField(upload_to="gallery/")
    caption = models.CharField(max_length=255)
    link = models.URLField(blank=True, null=True)  # New optional link field
    date_uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption


class LibraryDocument(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='library_docs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%b %Y')}"
