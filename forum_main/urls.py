from django.urls import path

from forum_main.views import forum_view, create_thread, my_threads, edit_thread, delete_thread, thread_details

urlpatterns = [
    path('', forum_view, name='index'),
    path('create/', create_thread, name='create thread'),
    path('my_threads/', my_threads, name='my threads'),
    path('edit/<int:pk>/', edit_thread, name='edit thread'),
    path('delete/<int:pk>/', delete_thread, name='delete thread'),
    path('details/<int:pk>', thread_details, name='thread details')
]