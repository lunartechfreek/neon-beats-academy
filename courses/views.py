from django.shortcuts import render, get_object_or_404
from .models import Course, CourseTier

def all_courses(request):
    """ A view to show all courses, including sorting and search queries """

    courses = Course.objects.all()
    tiers = CourseTier.objects.all()

    # To allow tier filtering and to render tier buttons
    if request.GET.get('tier'):
        selected_tier = request.GET['tier']
        courses = courses.filter(tier__tier_name=selected_tier)
    else:
        selected_tier = None

    context = {
        'courses': courses,
        'current_tiers': tiers,
        'selected_tier': selected_tier,
    }

    return render(request, 'courses/courses.html', context)


def course_detail(request, course_id):
    """ A view to show individual course details """

    course = get_object_or_404(Course, pk=course_id)

    context = {
        'course': course,
    }

    return render(request, 'courses/course_detail.html', context)