from django.shortcuts import render, redirect
from collection.forms import ThingForm
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

#section on adding content via public site
def edit_thing(request, slug):
    #grabbing the object
    thing = Thing.objects.get(slug=slug)
    # setting the form being used
    form_class = ThingForm
    # if we are coming to this view from a submitted form,
    if request.method == 'POST':
        # grab the data from the submitted form
        form = form_class(data=request.POST, instance=thing)
        if form.is_valid():
            #save the new data
            form.save()
            return redirect('thing_detail', slug=thing.slug)
        
        
    #otherwise just create the form
    else:
        form = form_class(instance=thing)
    
    # and render the template
    return render(request, 'things/edit_thing.html', {
        'thing': thing,
        'form': form,
    })
