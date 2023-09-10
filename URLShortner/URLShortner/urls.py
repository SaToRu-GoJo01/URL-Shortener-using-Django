from django.contrib import admin
from django.urls import path,include
from root.views import createUrl

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('root.urls'))
]
