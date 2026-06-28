from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ContactMessageForm


def index(request):
    if request.method == "POST":
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been saved.")
            return redirect("contact:index")
    else:
        form = ContactMessageForm()

    return render(request, "contact/contact_form.html", {"page_title": "Contact", "page_tag": "contact", "page_body": "Messages are stored in the database for backend handling.", "form": form})