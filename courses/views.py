from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Course, CourseTier
from .forms import CourseForm

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


@login_required
def add_course(request):
    """ Add a course to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admin can do that.')
        return redirect(reverse('home'))
        
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        course_name = request.POST.get('name', 'course')
        if form.is_valid():
            course = form.save()
            messages.success(request, f'Successfully added course: {course.name}!')
            return redirect(reverse('course_detail', args=[course.id]))
        else:
            messages.error(request, f'Failed to add course: "{course_name}". Please ensure the form is valid.')
    else:
        form = CourseForm()
        
    template = 'courses/add_course.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_course(request, course_id):
    """ Edit a course in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admin can do that.')
        return redirect(reverse('home'))

    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated {course.name}!')
            return redirect(reverse('course_detail', args=[course.id]))
        else:
            messages.error(request, f'Failed to update {course.name}. Please ensure the form is valid.')
    else:
        form = CourseForm(instance=course)
        messages.info(request, f'You are editing {course.name}')

    template = 'courses/edit_course.html'
    context = {
        'form': form,
        'course': course,
    }

    return render(request, template, context)


@login_required
def delete_course(request, course_id):
    """ Delete a course from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admin can do that.')
        return redirect(reverse('home'))

    course = get_object_or_404(Course, pk=course_id)
    course_name = course.name 
    course.delete()
    messages.success(request, f'Course "{course_name}" deleted!')
    return redirect(reverse('courses'))

