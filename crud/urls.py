from django.contrib import admin
from django.urls import path
from api_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuinfo/', views.Student_info.as_view()),
    path('stuinfo/<int:pk>', views.Student_info.as_view()),
]
