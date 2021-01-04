from django.urls import path
from webs import views as webs_views

urlpatterns = [
    path('Webs/posts/', webs_views.return_info)
]
