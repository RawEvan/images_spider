from django.shortcuts import render

# Create your views here.

def ranklist(request):
    if request.method == 'POST':        # when POST
        form = siteForm(request.POST)

        if form.is_valid():
            site = form.cleaned_data['site']
            photo_list = mySpider.getImg(site)
            return render(request, u'myalbum/myalbum.html', {'form': form,
                                                     'photo_list': photo_list,
                                                     'site': site})
        else:   # when POST is invalid
            form = siteForm()
            site = defaultUrl
            photo_list = mySpider.getImg(site)
            return render(request, u'myalbum/myalbum.html', {'form': form,
                                                     'photo_list': photo_list,
                                                     'site': site})
            
    else:       # when not POST , just by /url/(.+?)
        return render(request, u'ranklist/ranklist.html')
