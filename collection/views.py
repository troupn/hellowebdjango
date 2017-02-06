from django.shortcuts import render
from collection.models import Thing

#the rewritten view
def index(request):
    things = Thing.objects.all()
    return render(request, 'index.html', {
        'things': things,
    })
    
def thing_detail(reqeust, slug):
    #grab the object...
    thing = Thing.objects.get(slug=slug)
    #and pass to the template
    return render(reqeust, 'things/thing_detail.html', {
        'thing': thing,
    })