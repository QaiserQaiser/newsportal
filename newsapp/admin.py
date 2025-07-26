from django.contrib import admin
from .models import NewsletterSubscriber

# Register your models here.

@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at', 'is_active')
    list_filter = ('is_active', 'subscribed_at')
    search_fields = ('email',)
    readonly_fields = ('subscribed_at',)
    list_per_page = 20
    date_hierarchy = 'subscribed_at'
