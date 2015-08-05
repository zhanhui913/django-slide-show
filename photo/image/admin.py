from django.contrib import admin

from .models import Image

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields':['caption']}),
		('Description',      {'fields':['description']}),
		('Date information', {'fields':['upload_date'], 'classes':['collapse']}),
		('Favorite',         {'fields':['is_fav']}),
	]
	list_display = ('caption', 'description', 'upload_date', 'is_fav')
	list_filter = ['is_fav']
	search_fields = ('caption','description')

admin.site.register(Image, ImageAdmin)


