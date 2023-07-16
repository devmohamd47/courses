from django.shortcuts import render
from .models import Course, TeachRequest, Post, MsgRequest
from .forms import JoinAsLect, SendMsg
from django.core.paginator import Paginator
from django.contrib import messages
# Create your views here.

def index(request):
    courses = Course.objects.all().order_by('cid').values().reverse()
    context = {
        "courses": courses
    }
    return render(request, "all_courses.html", context)




def cdetails(request):

    cid = request.GET['cid']
    newprice = "ERR"
    course = Course.objects.get(cid=cid)
    discountok = course.discount > 0
    if discountok:
        newprice = course.price - (course.discount/100) * course.price

    context = {
        "course":course,
        "newprice":newprice,
        "discountok":discountok,
    }
    #context['type'] = course[0]
    return render(request, "course_details.html", context)

def join_as_lect(request):
    form = JoinAsLect()
    if request.method == "POST":
        print(request.POST['name'])
        form = JoinAsLect(request.POST)
        if form.is_valid():
             
            pc = TeachRequest(
                name = request.POST['name'],
                phone = request.POST['phone'],
                description = request.POST['description']
            )
             
            pc.save()
            messages.success(request, 'شكرا, تم تسجيل معلوماتك')
        else:
            messages.error(request, 'عذرا, يوجد خطأ في بياناتك!')
            return render(request, "join_as_lect.html")
    context = {
        
    }
    return render(request, "join_as_lect.html", context)



def latest_news(request):
    queryset = Post.objects.all().order_by('-created_at')

    paginator = Paginator(queryset, 5)  # Show 5 posts per page

    page_number = request.GET.get('page')  # Get the current page number from the request parameters
    page_obj = paginator.get_page(page_number)  # Get the corresponding page object

    context = {'page_obj': page_obj}
    return render(request, 'latest_news.html', context)


def news_post(request):
    pid = request.GET['pid']
    print(pid)
    post = Post.objects.get(id=pid)

    context = {
        'post':post
    }
    return render(request, 'news_post.html', context)


def custom_page_not_found(request, exception):
    return render(request, '404.html', status=404)

def contact(request):
    form = SendMsg()
    if request.method == "POST":
        form = SendMsg(request.POST)
        print(request.POST['name'], request.POST['phone'], request.POST['msg'])
        print(form.errors)
        if form.is_valid():
           
            pc = MsgRequest(
                name = request.POST['name'],
                phone = request.POST['phone'],
                msg = request.POST['msg']
            )
             
            pc.save()
            messages.success(request, 'شكرا, تم تسجيل معلوماتك')
        else:
            messages.error(request, 'عذرا, يوجد خطأ في بياناتك!')
            return render(request, "contact.html")
    return render(request, 'contact.html')