from django.forms import ModelForm
from .models import URLS


class URLForm(ModelForm):
    class Meta:
        model = URLS
        fields = ['long_url']