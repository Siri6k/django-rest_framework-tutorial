
from django.contrib import admin
from django.urls import path, include
import snippets.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(snippets.urls)),
]
