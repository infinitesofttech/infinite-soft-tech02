from django.contrib import admin
from . models import Project, Service, TeamMember, Product

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'client', 'date_completed')
    list_filter = ('category', 'date_completed')
    search_fields = ('title', 'description', 'client')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'created_at')
    list_filter = ('role',)
    search_fields = ('name', 'bio')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'created_at')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
