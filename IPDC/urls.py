from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('investor_dashboard', views.investor_dashboard, name='dash'),
    path('park_admin_dashboard', views.park_admin_dashboard, name='dash'),
    path('manager_dashboard', views.manager_dashboard, name='dash'),
    path('board_dashboard', views.board_dashboard, name='dash'),
    path('oiib_dashboard', views.oiib_dashboard, name='dash'),
    #path('', views.profilepage, name='profilepage'),
    path('land_request/', views.landpage, name='landpage'),
    path('submitfile/',views.filesubmission,name='filesubmit'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutpage,name="logout"),
]



