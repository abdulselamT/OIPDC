from . import views
from django.urls import path

urlpatterns = [
    path('', views.profilepage, name='profilepage'),
    path('land_request/', views.landpage, name='landpage'),
    path('submitfile/',views.filesubmission,name='filesubmit'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutpage,name="logout"),
]