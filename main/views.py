from available_courses.models import Course
from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Q


def IndexPageView(request):

    if request.method == "POST":
        post_values = list(request.POST.values())
        keyword = post_values[1]
        courses = Course.objects.filter(Q(name__icontains=keyword) | Q(trainer__icontains=keyword) | Q(type=keyword))
        context = {
        "courses": courses
    }
        return render(request, "all_courses.html", context)
    courses = Course.objects.filter(selected=True)
    context = {
        "courses": courses
    }
    return render(request, 'main/index.html', context)


class ChangeLanguageView(TemplateView):
    template_name = 'main/change_language.html'
