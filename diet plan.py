def diet(request):
    diet_data = [
        {"meal": "Breakfast", "food": "Oats, Milk"},
        {"meal": "Lunch", "food": "Rice, Chicken"},
        {"meal": "Dinner", "food": "Salad"}
    ]
    return render(request, 'diet.html', {'diet': diet_data})
