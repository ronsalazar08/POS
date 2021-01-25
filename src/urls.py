from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from . import views as src_views

admin.site.site_header = "STORE"
admin.site.site_title = "STORE"
admin.site.index_title = "Welcome to STORE Admin Page"
admin.site.enable_nav_sidebar = False
admin.site.site_url = "/dashboard"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', src_views.dashboard, name='dashboard'),
    path('employee/', include('apps.employee.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]
