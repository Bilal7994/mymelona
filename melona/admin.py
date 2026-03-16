from django.contrib import admin

# Register your models here.

from .models import ContactEnquiry


@admin.register(ContactEnquiry)
class ContactEnquiryAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'phone', 'email', 'subject')