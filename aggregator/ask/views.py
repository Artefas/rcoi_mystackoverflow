from django.shortcuts import render

# Create your views here.

def main(request):
    user_auth = request.GET.get("user")
    return render(request,'ask/main.html', context={"user":user_auth})

def tags(request):
    user_auth = request.GET.get("user")
    return render(request,'ask/tags.html', context={"user":user_auth})

def login(request):
    user_auth = request.GET.get("user")
    return render(request, 'ask/login.html', context={"user":user_auth})

def signup(request):
    user_auth = request.GET.get("user")
    return render(request, 'ask/signup.html', context={"user":user_auth})

def ask(request):
    user_auth = request.GET.get("user")
    return render(request, 'ask/ask.html', context={"user": user_auth})

def question(request, question_id):
    user_auth = request.GET.get("user")
    return render(request, 'ask/question.html', context={"user": user_auth})



