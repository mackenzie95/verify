from django.urls import path
from . import views


from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
        path('', views.coin),
        path('coinbase/', views.coinbase),
        ]




urlpatterns += staticfiles_urlpatterns()
