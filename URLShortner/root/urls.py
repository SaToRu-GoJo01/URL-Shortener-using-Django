from django.urls import path
from root.views import createUrl,routeToURL
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', createUrl),
    path('<slug:key>/',routeToURL)
]
