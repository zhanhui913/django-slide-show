from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import ListView, FormView, DetailView
from django.contrib import messages
from django.http import HttpResponseRedirect

from .models import Image, Favorite
from .forms import ImageForm

# Create your views here.
class ImageListView(ListView):
	model = Image
	context_object_name = 'images'

class ImageAddView(FormView):
	model = Image
	form_class = ImageForm
	success_url = reverse_lazy('image:home')
	template_name = 'image/index.html'

	def form_valid(self, form):
		form.save(commit = True)
		messages.success(self.request, 'File uploaded', fail_silently = True)
		return super(ImageAddView, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(ImageAddView, self).get_context_data(**kwargs)
		context['images'] = self.model.objects.all()
		return context

class ImageDetailView(DetailView):
	model = Image
"""
class FavoriteListView(ListView):
	model = Favorite
	context_object_name = 'favorites'
	template_name = 'image/list_favorite_images.html'
"""

def favorite(request, pk):
	"""
	p = get_object_or_404(Image, pk = pk)
	p.favorite_set.post(pk=request.POST['pk'])
	print "favorited "+pk+" -> "+p
	p.save()
	return HttpResponseRedirect(reverse('image:imageDetail'))
	"""
	print "favorited "+pk
	return HttpResponseRedirect(reverse('image:imageDetail'))