
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('AppCoder/', include('AppCoder.urls', namespace='AppCoder')),
    path('', include('AppCoder.urls')),

]
