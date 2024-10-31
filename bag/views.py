from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

from courses.models import Course

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add the specified course to the shopping bag """

    course = Course.objects.get(pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    # Add course to the bag without quantity
    bag[item_id] = 1  # Only add one instance of each course

    request.session['bag'] = bag
    messages.success(request, f'Added {course.name} to your bag')

    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        bag = request.session.get('bag', {})
        
        # Remove the item directly
        if item_id in bag:
            bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
