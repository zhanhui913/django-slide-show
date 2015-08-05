from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
	"""
	Upload files with this form
	"""
	class Meta:
		model = Image
		fields = ['path','caption','description','upload_date']

class FavForm(forms.ModelForm):
	class Meta:
		model = Image
		fields = ['is_fav']