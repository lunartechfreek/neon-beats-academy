from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages

from courses.models import Course


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add the specified course to the shopping bag """

    course = get_object_or_404(Course, pk=item_id)
    # default to home if redirect_url is missing
    redirect_url = request.POST.get('redirect_url', '/')
    bag = request.session.get('bag', {})

    # Check if the course is already in the bag
    if str(item_id) in bag:
        messages.error(request, f'{course.name} is already in your bag.')
        return redirect(redirect_url)

    # Add course to the bag
    bag[str(item_id)] = 1  # Only add one instance of each course
    request.session['bag'] = bag
    messages.success(request, f'Added {course.name} to your bag')

    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        course = get_object_or_404(Course, pk=item_id)
        bag = request.session.get('bag', {})

        # Remove the item directly
        if item_id in bag:
            bag.pop(item_id)
            messages.success(request, f'Removed {course.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
