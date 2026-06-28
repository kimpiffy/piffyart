from django.shortcuts import render


def index(request):
    return render(request, "section_page.html", {"page_title": "Personal Practice", "page_tag": "personal", "page_body": "A personal practice page for process notes, experiments, and reflective work."})