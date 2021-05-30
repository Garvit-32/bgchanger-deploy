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

    final_image = process(
        foreground=fileObj_f, background=fileObj_b)

    in_mem_file = BytesIO()
    final_image.save(in_mem_file, format='PNG')
    val = ContentFile(in_mem_file.getvalue())

    image_file = InMemoryUploadedFile(
        val, None, 'foo.jpeg', 'image/jpeg', val.tell, None)

    outputName = fs.save('result/output.png', image_file)
    output_url = fs.url(outputName)

    context['filePathName'] = output_url
    return render(request, 'deployApp/index.html', context)
