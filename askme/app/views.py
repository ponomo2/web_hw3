import random
from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
def index(request):
    qattributes = []
    for i in range(1, 30):
        qattributes.append({
            'title': 'title' + str(i),
            'id': i,
            'text': 'text' + str(i),
            'tags': ['one'+str(i), 'two'+str(i), 'three'+str(i)],
            'answerNum': random.randint(2, 7),
            'dislikes': random.randint(2, 10),
            'likes': random.randint(2, 20)
        })


    paginator = Paginator(qattributes,10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {
        'tags': ['first', 'second', 'third'],
        'members': ['member1', 'member2', 'member3'],
        'page_obj': page_obj
    }
    return render(request, 'index.html', data)

def question(request):
    return render(request, 'base.html')

def tag(request):
    return render(request, 'base.html')

def login(request):
    return render(request, 'base.html')

def signup(request):
    return render(request, 'base.html')

def ask(request):
    return render(request, 'base.html')

def settings(request):
    return render(request, 'base.html')

# def paginate(objects_list, request, per_page=10):
#     # do smth with Paginator, etc…
#     return page