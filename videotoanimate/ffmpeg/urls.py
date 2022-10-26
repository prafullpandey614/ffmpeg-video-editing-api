
from django.urls import path
from . import views
urlpatterns = [
    path('', views.ApiOverView.as_view()),
    path('upload-video/',views.FileUpload.as_view()),
    path('convert-video/<slug:pk>/',views.FileConvert.as_view()),
    path('output-video/<slug:pk>/',views.RetrieveFileView.as_view()),
    # path('see-output/<int:pk>/',views.OutputViewSet.as_view({'get': 'list'})),
    # path('file-convert/',views.FileConvert.as_view()),
]
