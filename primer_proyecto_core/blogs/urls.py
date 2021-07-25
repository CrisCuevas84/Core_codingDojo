from django.urls import path

from blogs.views import index, root, new, show, edit, create, destroy

urlpatterns = [
    path('blogs/<int:numero>/delete/', destroy),
    path('blogs/create/', create),
    path('', root),
    path('blogs/', index),
    path('blogs/<int:numero>/edit/', edit),
    path('blogs/<int:numero>/', show),
    path('blogs/new/', new),
    # path('', index),
]
