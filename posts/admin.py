"""Posts admin classes."""

# Django
from django.contrib import admin

#Models
from posts.models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	"""Post admin."""
	list_display = ('pk','user','profile','title','photo')
	list_display_links = ('pk','profile','photo')
	list_editable = ('user','title')
	search_fields = (
		'title', 
		'user__first_name',
		'user__last_name'
	)

	list_filter = (
		'created',
		'modified',
	)