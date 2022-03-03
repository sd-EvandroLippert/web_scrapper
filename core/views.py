from typing import Any, Dict
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import FormView

from core.scrapy import Scraper

from .models import ProxyLists


class IndexView(FormView):
    template_name = "index.html"
    success_url = reverse_lazy("index")

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        proxy = ProxyLists.objects.all()
        return super().get(request, {'proxy': proxy},  *args, **kwargs)


    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        pop_db = request.POST.get("bulkcreate")
        clean_db = request.POST.get("bulkdelete")
        if pop_db:
            results = Scraper().crawler()
            bulk_create_list = [ProxyLists(**result) for result in results]
            ProxyLists.objects.bulk_create(bulk_create_list)
        elif clean_db:
            ProxyLists.objects.all().delete()

        return super().post(request, *args, **kwargs)
