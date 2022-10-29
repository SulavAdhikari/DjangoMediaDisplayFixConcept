This project is meant to be an Example on how to fix a problem on django



this is not recommended because hosting a file like this without precaution could lead to directory traversal attack but this is for those who dont have a different server to host files and are using shared hosting to host their django site

The problem is that you cannot display media and static files in production mode.
There are modules you can use to fix the issue for static files like whitenoise.
But the problem still arises for media files like images
So I used django rest framework to return a HttpResponse containing a file with the content type application/octet-stream
So when you try to directly visit the page containing the file only it downloads it

for example :

localhost:8000/media/filename.ext 

Now if this is an image and you want to display it then you can set the content type to "image/jpg" or "imange/png" depending on the type of image