from django.shortcuts import render

# Create your views here.
def home(request):
    
    students = [
    {
        "name": "John Doe",
        "age": 20,
    },
    {
        "name": "Jane Doe",
        "age": 13,
    },
    {
        "name": "John Smith",
        "age": 11,
    },
    {
        "name": "Jane Smith",
        "age": 24,
    }
    ]
    return render(request, "index.html", context={"students": students, "title": "Home"})

def about(request):
    text = '''    
    Lorem ipsum dolor, sit amet consectetur adipisicing elit. Impedit, optio perferendis magni saepe aliquid corrupti ducimus iste, illum nulla earum obcaecati itaque ab. Minus nemo, omnis fugit adipisci excepturi commodi.
    '''
    return render(request, "about.html", context={"title": "About", "text": text})

def contact(request):
    return render(request, "contact.html", context={"title": "Contact"})