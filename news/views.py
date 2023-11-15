from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm, SendEmail


# Create your views here.

def index(request):
    return HttpResponse("xin chao")


def add_post(request):
    a = PostForm()
    return render(request, 'news/add_news.html', {'f': a})


def submit_news(request):
    if request.method == "POST":
        g = PostForm(request.POST)
        if g.is_valid():
            g.save()
            return HttpResponse("Saved")
        else:
            return HttpResponse("not save")
    else:
        return HttpResponse("Don't post request")


def email_view(request):
    b = SendEmail()
    return render(request, 'news/email.html', {'f': b})

#Cach 1
# def process(request):
#     if request.method == "POST":
#         m = SendEmail(request.POST)
#         if m.is_valid():
#             tieude = m.cleaned_data['title']
#             email = m.cleaned_data['email']
#             noidung = m.cleaned_data['content']
#             cc = m.cleaned_data['cc']
#             context = {'tieude': tieude, 'email': email, 'noidung': noidung, 'cc': cc}
#             return render(request, 'news/print_email.html', context)
#         else:
#             return HttpResponse('form not validate')
#     else:
#         return HttpResponse("Don't Post method")


#Cach 2
def process(request):
    if request.method == "POST":
        m = SendEmail(request.POST)
        if m.is_valid():
            context = {'email_view': m}
            return render(request, 'news/print_email.html', context)
        else:
            return HttpResponse('form not validate')
    else:
        return HttpResponse("Don't Post method")
