from typing import Any, Dict
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth.models import User
from core.forms import CustomUsuarioCreateForm
from core.scrapy import Scraper

from .models import CustomUsuario, ProxyLists


class IndexView(FormView):
    template_name = "index.html"
    success_url = reverse_lazy("index")
    form_class = CustomUsuarioCreateForm

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        proxy = ProxyLists.objects.all()
        return render(request, self.template_name, {'proxys': proxy, 'form': self.form_class})


    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        populate = request.POST.get("populatedb")
        cadastrar = request.POST.get("cadastrar")
        pop_db = request.POST.get("bulkcreate")
        clean_db = request.POST.get("bulkdelete")
        username = request.POST.get("username")
        password = request.POST.get("password1")
        if populate:
            if pop_db:
                results = Scraper().crawler()
                bulk_create_list = [ProxyLists(**result) for result in results]
                ProxyLists.objects.bulk_create(bulk_create_list)
            elif clean_db:
                ProxyLists.objects.all().delete()
        elif cadastrar:
            if username and password:
                CustomUsuario.objects.create_user(username, password)
                return redirect('/admin')
        return redirect('index')
