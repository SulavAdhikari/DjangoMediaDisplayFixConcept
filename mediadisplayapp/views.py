from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import views
from rest_framework.response import Response
import os

from NewsPortal import settings
# Create your views here.


# this view accepts get request and returns file based on name
class FileReturnAPIView(views.APIView):
    
    def get(self, request, name):
        path = os.path.join(settings.MEDIA_ROOT, name)
        
        #to prevent directory traversal we need to check of it contains ../
        if "../" in path:
            return Response(status=403)
        file = open( path, 'rb')
        data = file.read()
        #if file does not exist the obviously it return 404 instead of empty result    
        if data == None:
            print(path)
            return Response(status=404)
        
        return HttpResponse(data, content_type = 'image/jpg')

        