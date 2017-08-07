from django.forms import ModelForm

from .models import ImageFile


class ImageUploadForm(ModelForm):
    class Meta:
        model = ImageFile
        fields = {'title', 'image'}
