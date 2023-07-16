from django.urls import path
from .views import index, cdetails, join_as_lect, latest_news, news_post, custom_page_not_found, contact

handler404 = custom_page_not_found

urlpatterns = [
    path('', index, name="cindex"),
    path('course_details', cdetails, name="cdetails"),
    path('join_as_lect', join_as_lect, name="join_as_lect"),
    path('latest_news', latest_news, name="latest_news"),
    path('news_post', news_post, name="news_post"),
    path('contact', contact, name="contact"),
    ]