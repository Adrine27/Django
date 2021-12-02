from django.contrib import admin
from .models import Category, Cigarette
from django.utils.safestring import mark_safe
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('title',)}
	list_display = ('id','title')
	list_display_links = ('id','title')
	search_fields = ('title',)


@admin.register(Cigarette)
class CigaretteAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('title',)}
	list_display = ('id','title','date','category','slug','photo','count','price','choices')
	list_display_links = ('title',)
	list_filter = ('category__title','date')
	search_fields = ('title','category__title')
	# readonly_fields = ('get_photo')
	# list_editable = 'choices'
	save_on_top = True
	fieldsets = (
		('Category',{
			'fields':(('category'),)
			}),
		('Title and Slug',{
			'fields':(('title','slug'),)
			}),
		('Date and Picture',{
			'fields':(('date','photo'),)
			}),
		# ('',{
		# 	'fields':('date',)
		# 	}),
		('Count and Price',{
			'fields':(('count','price'),)
			}),
		('Thickness and Description',{
			'fields':(('choices','description'),)
			}),
		('Nicotine and Xej',{
			'fields':(('nicotine','xej'),)
			})
		)
	def get_image(self,obj):
		return mark_safe(f'<img src = {obj.picture.url} width = "70" height = "70">')
	get_image.short_description = 'photo'



