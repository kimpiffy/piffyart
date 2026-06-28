from django.shortcuts import render


def home(request):
    blobs = [
        {"title": "About", "description": "Modal introduction to the studio, the rhythm, and the visual language.", "kind": "modal", "badge": "pop-up", "rotation": -5},
        {"title": "Personal Practice", "description": "A quieter lane for reflective, personal work and process sketches.", "url_name": "personal:index", "badge": "personal", "rotation": 4},
        {"title": "Web Design", "description": "The digital side: motion, structure, interaction, and responsive systems.", "url_name": "digital:index", "badge": "digital", "rotation": -2},
        {"title": "Creative Health", "description": "Community-facing work that stays warm, calm, and easy to approach.", "url_name": "community:index", "badge": "community", "rotation": 3},
        {"title": "Shop", "description": "A space for products, print runs, drop-based stock, and future storefronts.", "url_name": "shop:index", "badge": "store", "rotation": -4},
        {"title": "Contact", "description": "A direct route into the database-backed contact inbox.", "url_name": "contact:index", "badge": "message", "rotation": 5},
        {"title": "Accounts", "description": "Front-end login access for the private management area.", "url_name": "accounts:login", "badge": "admin", "rotation": -1},
    ]

    return render(request, "home.html", {"blobs": blobs})