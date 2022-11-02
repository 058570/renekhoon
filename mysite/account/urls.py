"""account URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from for_starter_api.views import *
from django.urls import path

urlpatterns = [
    path('users/', ManagerAccountListAPI.as_view()),
    path('users/<int:pk>', ManagerAccountList_DetailAPI.as_view()),
    path('login/', LoginAPI.as_view()),
    path('institution/', InstitutionListAPI.as_view()),
    path('institution/<int:pk>', InstitutionList_detailAPI.as_view()),
    path('notice/', NoticeAPI.as_view()),
    path('notice/<int:pk>', Notice_detailAPI.as_view()),
    path('softwareupdate/', SoftwareUpdateListAPI.as_view()),
    path('softwareupdate/<int:pk>', SoftwareUpdateList_detailAPI.as_view()),
]
