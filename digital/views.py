from django.shortcuts import render


def index(request):
    return render(request, "section_page.html", {"page_title": "Web Design", "page_tag": "digital", "page_body": "A digital studio page for responsive layouts, systems, and browser-first ideas."})