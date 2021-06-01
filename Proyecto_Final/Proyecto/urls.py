from django.urls import include, path


urlpatterns = [
    path('', include('Monitor.urls')),
    path('', include('Auth.urls')),
]
