import os
from io import BytesIO
from django.shortcuts import render
from django.core.files.base import ContentFile
from .bgchanger.main import process
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.uploadedfile import InMemoryUploadedFile
# Create your views here.


def remove():
    if os.path.exists('result/foreground.png'):
        os.remove("result/foreground.png")
    if os.path.exists('result/background.png'):
        os.remove("result/background.png")

    if os.path.exists('result/output.png'):
        os.remove("result/output.png")


def index(request):
    context = {'a': 1}
    return render(request, 'deployApp/index.html', context)


def predictImage(request):

    remove()
    context = {}

    try:
        fileObj_f = request.FILES['foreground']
        fileObj_b = request.FILES['background']
    except MultiValueDictKeyError:
        context['error_message'] = "Please select a image"
        return render(request, 'deployApp/index.html', context)

    fs = FileSystemStorage()
    filePathName = fs.save('result/foreground.png', fileObj_f)
    filePathName_f = fs.url(filePathName)

    fs = FileSystemStorage()
    filePathName = fs.save('result/background.png', fileObj_b)
    filePathName_b = fs.url(filePathName)

    final_image = process(
        foreground='result/foreground.png', background='result/background.png')

    in_mem_file = BytesIO()
    final_image.save(in_mem_file, format='PNG')
    val = ContentFile(in_mem_file.getvalue())

    image_file = InMemoryUploadedFile(
        val, None, 'foo.jpeg', 'image/jpeg', val.tell, None)

    outputName = fs.save('result/output.png', image_file)
    output_url = fs.url(outputName)

    context['filePathName'] = output_url
    context['filePathName_f'] = filePathName_f
    context['filePathName_b'] = filePathName_b
    return render(request, 'deployApp/index.html', context)
