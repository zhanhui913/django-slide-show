from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import ListView, FormView, DetailView
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Image
from .forms import ImageForm, FavForm

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

	def post(self, request, pk):
		fav_status = request.POST.get('fav', 'false')
		fav_value = False if fav_status.lower() == 'false' else True
		print "favoriting -> "+str(fav_value)
		instance = get_object_or_404(Image, pk=pk)
		instance.is_fav = fav_value
		instance.save()
		return HttpResponseRedirect(reverse_lazy('image:imageDetail', args=(pk)))

class FavList(ListView):
	print "favList"
	model = Image
	context_object_name = "favImages"
	template_name = 'image/image_favList.html'
	def get_queryset(self):
		"""
		Return all favorited images.
		"""
		return Image.objects.filter(is_fav=True)


	def post(self, request):
		print "posting on favList"
		pk = request.POST.get('pk')
		
		fav_status = request.POST.get('fav', 'false')
		fav_value = False if fav_status.lower() == 'false' else True

		instance = get_object_or_404(Image, pk=pk)
		instance.is_fav = fav_value
		instance.save()
		return HttpResponseRedirect(reverse_lazy('image:favoriteList'))