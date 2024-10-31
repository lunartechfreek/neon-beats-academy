from django.shortcuts import render, redirect

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add the specified course to the shopping bag """

    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    # Add course to the bag without quantity
    bag[item_id] = 1  # Only add one instance of each course

    request.session['bag'] = bag
    return redirect(redirect_url)
