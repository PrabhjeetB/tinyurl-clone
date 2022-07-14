from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from .models import TinyUrl
from tinyurl.utils.tiny import get_original_url, get_tinyurl


class TinyUrlListView(LoginRequiredMixin, ListView):
    model = TinyUrl
    context_object_name = "tinyurls"
    paginate_by = 10

    def get_queryset(self):
        return TinyUrl.objects.filter(user=self.request.user).order_by("created")


class TinyUrlCreateView(LoginRequiredMixin, CreateView):
    model = TinyUrl
    fields = ["original_url"]

    def form_valid(self, form):
        original_url = form.instance.original_url
        if original_url:
            short_url = get_tinyurl(original_url)
        form.instance.short_url = short_url
        form.instance.user = self.request.user
        return super().form_valid(form)


@login_required
@api_view(("GET",))
@renderer_classes((JSONRenderer, TemplateHTMLRenderer))
def get_original(request, short_url=None):
    print(f"Short url: {short_url}")
    original_url = get_original_url(short_url)
    if original_url:
        return HttpResponseRedirect(original_url)
    else:
        context = {}
        context["TINY_URL"] = short_url
        return render(request, "404.html", context)
