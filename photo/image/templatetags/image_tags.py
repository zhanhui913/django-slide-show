from django import template

register = template.Library()

@register.inclusion_tag('image/fav.html')
def fav_button(image, *args, **kwaargs):
	context = {
		'is_fav': image.favorites.all,
		'image': image
	}
	return context

