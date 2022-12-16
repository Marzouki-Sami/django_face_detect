from django.http import HttpResponse
from django.shortcuts import render
import cv2 as cv


def index(request):
    if request.method == 'POST' and request.FILES['myfile']:
        image = request.FILES['myfile']

        # save image as jpg
        with open('media/img.jpg', 'wb+') as destination:
            for chunk in image.chunks():
                destination.write(chunk)

        RED = (0, 0, 255)

        img = cv.imread('media/img.jpg')
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        path = 'cascade/haarcascade_frontalface_default.xml'
        face_detector = cv.CascadeClassifier(path)

        faces = face_detector.detectMultiScale(gray, 1.1, 4)
        for rect in faces:
            cv.rectangle(img, rect, RED, 2)

        # save the image
        cv.imwrite('media/face_detected.jpg', img)

    return HttpResponse(render(request, 'src/html/image_upload.html'))
