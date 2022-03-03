from django.contrib import admin

from core.models import ProxyLists
from core.scrapy import Scraper

# Register your models here.


@admin.register(ProxyLists)
class ProxyListsAdmin(admin.ModelAdmin):
    list_display = (
        "ip_address",
        "port",
        "protocol",
        "anonymity",
        "country",
        "region",
        "city",
        "uptime",
        "response",
        "speed",
        "last_checked",
    )
    search_fields = ("protocol", "country", "region")
