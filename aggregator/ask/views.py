from django.shortcuts import render

# Create your views here.

def main(request):
    user_auth = request.GET.get("user")
    return render(request,'ask/main.html', context={"user":user_auth})
