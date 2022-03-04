from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .classifier import Classifier
from .forms import ImageForm
from PIL import Image
from .models import ImgClass
from django.shortcuts import redirect


def main(request):
    form = ImageForm()
    return render(request, 'cnnclassifierapp/index.html', context={'form': form})


def get_output(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            image = Image.open(form.cleaned_data.get('image'))
            prediction = Classifier(image).classify()
            image_name = form.cleaned_data.get('image').name
            fss = FileSystemStorage()
            file = fss.save(image_name, form.cleaned_data.get('image'))
            image_path = fss.url(file)
            ImgClass.objects.create(img_path=image_path, img_classifier=prediction)
            return render(request, 'cnnclassifierapp/index.html',
                          context={'prediction': prediction, 'img_path': image_path, 'form': form})
