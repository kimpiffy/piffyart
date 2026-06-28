from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def dashboard(request):
    return render(request, "accounts/dashboard.html", {"page_title": "Dashboard", "page_body": "A protected admin-style landing zone for managing shop and contact activity."})