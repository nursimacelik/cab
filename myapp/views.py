from django.shortcuts import render, redirect
from .models import Post
from .models import Message
from .forms import SearchForm
from .forms import ContactForm
from django.db.models import Q 

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def home_page(request):
    posts = Post.objects.order_by('-read_count')[:3]
    return render(request, 'myapp/home_page.html', {'articles': posts})

def about(request):
    return render(request, 'myapp/about.html')

def services(request):
    return render(request, 'myapp/services.html')

def blog(request):
    posts = Post.objects.all()
    form = SearchForm()
    return render(request, 'myapp/blog.html', {'articles': posts, 'form':form})

def search(request):
    query = request.GET.get('q')
    posts = Post.objects.filter(Q(title__icontains=query) | Q(text__icontains=query))
    form = SearchForm()
    return render(request, 'myapp/blog.html', {'articles': posts, 'form':form})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    post.read_count += 1
    post.save()
    return render(request, 'myapp/post_detail.html', {'post':post})

def contact(request):
    if request.method == 'GET':
        form = ContactForm(data={'message':'Mesaj:'})
        form.fields['subject'].widget.attrs['label'] = 'message'

    else:
        print("else")
        form = ContactForm(request.POST)
        if form.is_valid():
            print("valid")
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            msg = form.save(commit=False)
            msg.save()
            return redirect('success')
    return render(request, "myapp/contact.html", {'form': form})

def success(request):
    return HttpResponse('Success! Thank you for your message.')