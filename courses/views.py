from django.shortcuts import render, get_object_or_404
from .models import Course, CourseTier

def all_courses(request):
    """ A view to show all courses, including sorting and search queries """

    courses = Course.objects.all()

    tiers = None

    if request.GET:
        if 'tier' in request.GET:
            tiers = request.GET['tier'].split(',')
            courses = courses.filter(tier__tier_name__in=tiers)
            tiers = CourseTier.objects.filter(tier_name__in=tiers)

    context = {
        'courses': courses,
        'current_tiers': tiers,
    }

    return render(request, 'courses/courses.html', context)


def course_detail(request, course_id):
    """ A view to show individual course details """

    course = get_object_or_404(Course, pk=course_id)

    context = {
        'course': course,
    }

    return render(request, 'courses/course_detail.html', context)