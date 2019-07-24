from django.contrib import admin

# Register your models here.

from .models import Mentee, Mentor, Blog

class MenteeAdmin(admin.ModelAdmin):
    list_display = ['id', 'nama', 'quotes']  
    list_display_links = ['nama']

class MentorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nama', 'quotes', 'experience']  
    list_display_links = ['nama']

class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'judul', 'tanggal']  
    list_display_links = ['judul']


admin.site.register(Blog, BlogAdmin)
admin.site.register(Mentee, MenteeAdmin)
admin.site.register(Mentor, MentorAdmin)