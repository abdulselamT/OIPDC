from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('investor_personal_information', views.investor_personal_information, name='investor_personal_information'),
    path('investor_project_information', views.investor_project_information, name='investor_project_information'),
    path('investor_file_information', views.investor_file_information, name='investor_file_information'),

    path('park_admin_dashboard', views.park_admin_dashboard, name='dash'),
    path('manager_dashboard', views.manager_dashboard, name='dash'),
    path('board_dashboard', views.board_dashboard, name='dash'),
    path('oiib_dashboard', views.oiib_dashboard, name='dash'),
    path('profile/', views.profilepage, name='profilepage'),
    path('land_request/', views.landpage, name='landpage'),
    path('submitfile/',views.filesubmission,name='filesubmit'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutpage,name="logout"),
]
