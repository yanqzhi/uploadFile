from django.shortcuts import render, redirect
from channels import Channel
from .forms import ImageUploadForm
from .models import ImageFile


# Create your views here.

def upload(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_file = form.save()
            notification = {
                'id':image_file.id,
            }
            Channel('create_thumbnail').send(notification)            
            return redirect('uploadImage:image_list')
    else:
        form = ImageUploadForm()

    return render(request, 'uploadImage/upload.html', {'form': form})


def image_list(request):
    images = ImageFile.objects.all()

    return render(request, 'uploadImage/imageList.html', {'images': images})
