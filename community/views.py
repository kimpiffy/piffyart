from django.shortcuts import render


def index(request):
    return render(request, "section_page.html", {"page_title": "Creative Health", "page_tag": "community", "page_body": "A community page for care-led work, collaboration, and grounded creative direction."})