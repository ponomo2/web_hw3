import random
from django.core.paginator import Paginator
from django.shortcuts import render


# Create your views here.
def index(request):
    page_obj = paginate(make_questions(True), request)
    data = {
        'tags_left': ['first', 'second', 'third'],
        'members': ['member1', 'member2', 'member3'],
        'page_obj': page_obj,
        'new_or_not': True
    }
    return render(request, 'index.html', data)


def hot(request):
    page_obj = paginate(make_questions(True), request)
    data = {
        'tags_left': ['first', 'second', 'third'],
        'members': ['member1', 'member2', 'member3'],
        'page_obj': page_obj,
        'new_or_not': False
    }
    return render(request, 'index.html', data)


def question(request, num):
    page_obj = paginate(make_questions(True), request, 3)
    data = {
        'title': 'title' + str(num),
        'id': num,
        'text': 'text' + str(num),
        'tags': ['one' + str(num), 'two' + str(num), 'three' + str(num)],
        'dislikes': random.randint(2, 10),
        'likes': random.randint(2, 20),
        'tags_left': ['first', 'second', 'third'],
        'members': ['member1', 'member2', 'member3'],
        'page_obj': page_obj,
        'number': num
    }

    return render(request, 'question.html', data)


def tag(request):
    return render(request, 'index.html')


def login(request):
    data = {
        'tags_left': ['first', 'second', 'third'],
        'members': ['member1', 'member2', 'member3']
    }
    return render(request, 'login.html', data)


def signup(request):
    data = {
        'tags_left': ['first', 'second', 'third'],
        'members': ['member1', 'member2', 'member3']
    }
    return render(request, 'signup.html', data)


def ask(request):
    data = {
        'tags_left': ['first', 'second', 'third'],
        'members': ['member1', 'member2', 'member3']
    }
    return render(request, 'ask.html', data)


def settings(request):
    data = {
        'tags_left': ['first', 'second', 'third'],
        'members': ['member1', 'member2', 'member3']
    }
    return render(request, 'settings.html', data)


def make_questions(sort_by):
    qattributes = []
    for i in range(1, 30):
        qattributes.append({
            'title': 'title' + str(i),
            'id': i,
            'text': 'text' + str(i),
            'tags': ['one' + str(i), 'two' + str(i), 'three' + str(i)],
            'answerNum': random.randint(2, 7),
            'dislikes': random.randint(2, 10),
            'likes': random.randint(2, 20)
        })
    return qattributes


def make_answers():
    qanswers = []
    for i in range(1, 10):
        qanswers.append({
            'id': i,
            'text': 'text' + str(i),
            'tags': ['one' + str(i), 'two' + str(i), 'three' + str(i)],
            'dislikes': random.randint(0, 5),
            'likes': random.randint(2, 8)
        })
    return qanswers


def paginate(objects_list, request, per_page=10):
    paginator = Paginator(objects_list, per_page)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return page
