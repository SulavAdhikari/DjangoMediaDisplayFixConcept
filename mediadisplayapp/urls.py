from django.urls import path

from .views import FileReturnAPIView

urlpatterns = [
    path('<str:name>',FileReturnAPIView.as_view()),
]

app_name = 'media'