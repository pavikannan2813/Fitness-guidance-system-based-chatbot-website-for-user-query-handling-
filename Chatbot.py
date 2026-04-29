from .models import Query

def chatbot(request):
    response = ""

    if request.method == "POST":
        msg = request.POST['message']
        data = Query.objects.filter(question__icontains=msg)

        if data.exists():
            response = data.first().answer
        else:
            response = "No result found"

    return render(request, 'chatbot.html', {'response': response})
