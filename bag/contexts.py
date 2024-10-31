from django.shortcuts import get_object_or_404
from courses.models import Course

def bag_contents(request):
    bag_items = []
    total = 0
    bag = request.session.get('bag', {})

    for item_id in bag.keys():
        course = get_object_or_404(Course, pk=item_id)
        total += course.price  # Only add the course price once
        bag_items.append({
            'item_id': item_id,
            'course': course,
        })

    grand_total = total
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'course_count': len(bag_items),  # Count of unique courses
        'grand_total': grand_total,
    }

    return context
