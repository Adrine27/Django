from django.contrib import admin
from .models import Category,New
from django.utils.safestring import mark_safe
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('title',)}
	list_display = ('id','title')
	list_display_links = ('title','id')
	search_fields = ('title',)


@admin.register(New)
class NewAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('title',)}
	list_display = ('id','title','category','date','status','get_image')
	list_display_links = ('title',)
	list_filter = ('category__title','date','author','status')
	search_fields = ('title','author','category__title',)
	readonly_fields = ('get_image',)
	save_on_top = True
	list_editable = ('status',)
	fieldsets = (
		('Categories',{
			'fields':(('category','additional_category'),)
			}),
		('Title and Slug',{
			'fields':(('title','slug'),)
			}),
		('Author and status',{
			'fields':(('author','status'),)
			}),
		('content',{
			'fields':(('content'),)
			}),
		('Date and Picture',{
			'fields':(('picture','get_image'),)
			}),
		('',{
			'fields':('date',)
			}),
	)

	def get_image(self,obj):
		return mark_safe(f'<img src={obj.picture.url} width="70" height = "70"')

	get_image.short_description = 'Picture'

admin.site.site_title = 'One Planet Admin'
admin.site.site_header = 'One Planet Admin'