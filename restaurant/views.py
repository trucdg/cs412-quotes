from django.shortcuts import render

import time, random

# Create your views here.

def main(request):
    """
    Handle requests to url endpoint /restaurant/main
    Render with template main.html
    """
    # Context data for the main page (name, location, hours, photos)
    context = {
        "current_time": time.ctime(),
        'name': 'Pho 89 Brockton',
        'location': '708 Belmont St, Brockton, MA 02301',
        'hours': ['Mon-Fri: 9:00am - 10:00pm', 'Sat-Sun: 10:00am - 11:00pm'],
        'photos': [
            'https://www.enterprisenews.com/gcdn/authoring/authoring-images/2024/05/18/NENT/73749325007-05182024-mv-brockton-food-21.JPG?width=1200&disable=upscale&format=pjpg&auto=webp', 
            'https://s3-media0.fl.yelpcdn.com/bphoto/J75xZymFFmAeHDwMxcM8sw/o.jpg',
            "https://www.dailynews.com/wp-content/uploads/2023/01/LDN-L-DINE-PHO-0113-01-03.jpg?w=525"]
    }
    return render(request, 'restaurant/main.html', context)

def order(request):
    """
    Handle requests to url endpoint /restaurant/order
    Render with template order.html
    Display the order page where customers can select pho noodle soup and other Vietnamese dishes.
    Pass a random "daily special" item to the order.html template
    """

    # Dict of regular dishes and their prices
    dishes = {
        'Wonton Soup': 8,
        'Egg Rolls': 6,
        'Beef Noodle Soup with Brisket': 15,
        'Special Combination Beef Noodle Soup': 16,
    }

    # Extra toppings for the special combination and their prices
    toppings = {
        'Extra Vegetables': 2,
        'Extra Meatballs': 3,
        'Extra Brisket': 4,
        'Tendon': 3,
    }

    # Dict of special dishes
    specials = {
        'Spring Rolls': 7,
        'Sate Beef Udon': 16,
        'Grilled Chicken Vemicelli': 15
    }

    # Randomly select a daily special
    daily_special_name = random.choice(list(specials.keys()))
    daily_special_price = specials[daily_special_name]

    # argument for the order.html template
    context = {
        "current_time": time.ctime(),
        'dishes' : dishes,
        'toppings' : toppings,
        'daily_special' : {
            'name' : daily_special_name,
            'price' : daily_special_price
        }
    }

    return render(request, 'restaurant/order.html', context)


def submit(request):
    """
    Handle the form submission
    Read data from the request and send it back to confirmation.html
    """

    template_name = 'restaurant/confirmation.html'

    # Handle form submission
    if request.POST:
        # get selected items and toppings
        print(request.POST)
        #selected_items = request.POST.getlist('items')

    return render(request, template_name)