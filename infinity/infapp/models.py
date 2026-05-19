from django.db import models

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('web', 'Web Development'),
        ('mobile', 'Mobile Apps'),
        ('ai', 'AI Solutions'),
        ('software', 'Software'),
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    short_description = models.CharField(max_length=500, blank=True)
    image = models.CharField(max_length=255, help_text="Path to image file")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    client = models.CharField(max_length=255, blank=True)
    technologies = models.CharField(max_length=500, blank=True, help_text="Comma-separated list")
    date_completed = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Service(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    short_description = models.CharField(max_length=500, blank=True)
    image = models.CharField(max_length=255, help_text="Path to image file", blank=True)
    features = models.TextField(help_text="Comma-separated list of features")
    icon = models.CharField(max_length=100, blank=True, help_text="Icon class name")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    ROLE_CHOICES = [
        ('founder', 'Founder'),
        ('developer', 'Developer'),
        ('designer', 'Designer'),
        ('manager', 'Manager'),
        ('specialist', 'Specialist'),
    ]

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    bio = models.TextField()
    short_bio = models.CharField(max_length=300, blank=True)
    image = models.CharField(max_length=255, help_text="Path to image file")
    expertise = models.CharField(max_length=500, blank=True, help_text="Comma-separated list")
    social_links = models.CharField(max_length=500, blank=True, help_text="JSON format for social links")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('software', 'Software'),
        ('hrms', 'HRMS'),
        ('ecommerce', 'E-Commerce'),
        ('retail', 'Retail'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    short_description = models.CharField(max_length=500, blank=True)
    image = models.CharField(max_length=255, help_text="Path to image file")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    features = models.TextField(help_text="Comma-separated list of features")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
