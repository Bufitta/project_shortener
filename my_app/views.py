from django.shortcuts import render
from forms import ShortenerForm
from random import choice
import string
from models import ShortUrl
from django.http import HttpResponse
from django.shortcuts import redirect

def shortener(request):
    link = ShortUrl.objects.filter()
    if request.method == 'POST':
        form = ShortenerForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if ShortUrl.objects.filter(original_url = data['original_url']).count()>0:
                shortUrl = ShortUrl.objects.filter(original_url = data['original_url']).get()
                context = {'shortener': ShortenerForm(), 'shortUrl': shortUrl, 'links': link}
                return render(request, 'result.html', context)
            else:
                symbols = string.digits + string.letters
                key = ''.join(choice(symbols) for item in range(7))
                short_url = 'http://127.0.0.1:8000/%s' %key
                new_shortUrl = ShortUrl.objects.create(original_url = data['original_url'], short_url=short_url, clicks=0)
                context = {'shortener': ShortenerForm(),'links': link, 'new_shortUrl': new_shortUrl}
                return render(request,'result.html', context)
        context = {'shortener': form, 'links': link}
        return render(request, 'result.html', context)
    else:
        context = {'shortener': ShortenerForm(), 'links': link}
        return render(request, 'result.html', context)

def my_redirect(request, key):
    shortUrls = ShortUrl.objects.filter().values()
    for shortUrl in shortUrls:
        if key in shortUrl['short_url']:
            url = shortUrl['original_url']
            clicks = shortUrl['clicks']
            clicks+=1
            ShortUrl.objects.filter(original_url=url).update(clicks=clicks)
            return redirect(url)
    context = {}
    return render(request, 'error.html', context)