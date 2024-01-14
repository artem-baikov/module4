from django.shortcuts import render, redirect
<<<<<<< HEAD
from django.urls import reverse, reverse_lazy
from .forms import AdvertisementForm
from .models import Advertisement
from django.contrib.auth.decorators import login_required
=======
from django.http import HttpResponse
from .models import Advertisement
from .forms import AdvertisementForm
from django.urls import reverse
>>>>>>> origin/main

def index(request):
    advertisements = Advertisement.objects.all()
    context = {'advertisements': advertisements}
    return render(request, 'app_les4/index.html', context)

def top_sellers(request):
    return render(request, 'app_les4/top-sellers.html')

def advertisement(request):
    return render(request, 'app_les4/advertisement.html')

@login_required(login_url=reverse_lazy('login'))
def advertisement_post(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisement(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'app_les4/advertisement-post.html', context)