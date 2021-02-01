from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import SafariAccount


class Dashboard(View):
    template_name = 'dashboard/home.html'

    def get(self, request):
        return render(request, self.template_name)


def GetSafariAccount(request):
    data = list(SafariAccount.objects.filter(is_expired=False).values())
    return JsonResponse(data, safe=False)