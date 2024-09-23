from django.urls import path
from . import views

# Define the URL patterns for the quotes app.
# Each URL pattern maps to a view function in views.py
urlpatterns = [
    # Main page: Displays a random quote and image.
    path("", views.quote, name="quote"),
    # 1 quote page: Displays a random quote and image.
    path("quote", views.quote, name="quote"),
    # Displays all quotes and images.
    path("show_all/", views.show_all, name="show_all"),
    # Displays info about Barack Obama
    path("about/", views.about, name="about"),
]
