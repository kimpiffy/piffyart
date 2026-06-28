from django.shortcuts import render


def index(request):
    return render(
        request,
        "section_page.html",
        {
            "page_title": "Industry",
            "page_tag": "industry",
            "page_body": "A placeholder section for industry-facing work, case studies, and future expansion.",
        },
    )