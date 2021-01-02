from django.urls import path
from files import exercise as local_views
from webs import views as webs_views

urlpatterns = [
    path('hello-world/', local_views.hi),
    path('optional/<int:age>/<str:name>/', local_views.optional),

    path('Webs/posts/', webs_views.return_info)
]
