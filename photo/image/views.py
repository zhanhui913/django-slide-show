from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import ListView, FormView, DetailView
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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

	def post(self, request, pk):
		fav_status = request.POST.get('fav', 'false')
		print "favoriting -> "+fav_status.lower()

		if fav_status.lower() == "false":
			# Removing this image from favorite table
			i = Image.objects.get(pk=pk)
			f = Favorite.objects.get(image=i)
			f.delete()

		else:
			# Adding this image to favorite table
			f = Favorite()
			f.image = Image.objects.get(pk=pk)
			
			#Find the highest order and +1
			highest_order_image = Favorite.objects.order_by("-order")[0]
			f.order = highest_order_image.order + 1
			f.save()

		return HttpResponseRedirect(reverse_lazy('image:imageDetail', args=(pk)))

class FavList(ListView):
	print "favList"
	model = Favorite
	context_object_name = "favImages"
	template_name = 'image/image_favList.html'
	
	def get_queryset(self):
		# Return all favorited images.
		return Favorite.objects.all().order_by('order')

	def post(self, request):
		ref = request.POST.get('ref')

		# POST for unfavoriting
		if ref == "favorite":
			image_pk = request.POST.get('pk')
			
			i = Image.objects.get(pk=image_pk)
			f = Favorite.objects.get(image=i)

			exist = False if f is None else True
			
			if exist:
				# Removing this image from favorite table
				f.delete()
			else:
				# Adding this image to favorite table
				f = Favorite()
				f.image = Image.objects.get(pk=image_pk)
				f.save()

		# POST for sorting
		elif ref == "sort":
			new_order = request.POST.getlist('new_order[]')

			# Update order for all favorited images
			for w in new_order:
				split = w.split("-")
				order = split[0]
				image_pk = split[2]

				i = Image.objects.get(pk=image_pk)
				f = Favorite.objects.get(image=i)
				f.order = order
				f.save()

		return HttpResponseRedirect(reverse_lazy('image:favoriteList'))