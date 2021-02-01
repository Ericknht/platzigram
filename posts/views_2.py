
from django.contrib.auth.decorators import login_required


# Utilites
"""
from datetime import datetime

posts = [
	{
	    'title': 'Mont Blanc',
	    'user': {
	        'name': 'Yésica Cortés',
	        'picture': 'https://picsum.photos/60/60/?image=1027'
	    },
	    'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
	    'photo': 'https://picsum.photos/800/600?image=1036',
	},
	{
	    'title': 'Via Láctea',
	    'user': {
	        'name': 'Christian Van der Henst',
	        'picture': 'https://picsum.photos/60/60/?image=1005'
	    },
	    'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
	    'photo': 'https://picsum.photos/800/800/?image=903',
	},
	{
	    'title': 'Nuevo auditorio',
	    'user': {
	        'name': 'Uriel (thespianartist)',
	        'picture': 'https://picsum.photos/60/60/?image=883'
	    },
	    'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
	    'photo': 'https://picsum.photos/500/700/?image=1076',
	}
]"""


# fue reemplazado por la clase PostDetailView
@login_required
def list_posts(request):
	"""List existing posts."""
	content = []
	for post in posts:
		content.append("""
			<p><strong>{name}</strong></p>
			<p><small>{user} - {timestamp}</small></p>
			<figure><img src="{picture}"/></figure>
			""".format(**post))


	return HttpResponse('<br/>'.join(content))
	posts = Post.objects.all().order_by('-created')

	return render(request,'posts/feed.html', {'posts': posts})

# Fue reemplazado por CreatePostView
@login_required
def create_post(request):
	"""Create new post view."""
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('posts:feed')
	else:
		form = PostForm()

	return render(
		request=request,
		template_name='posts/new.html',
		context={
			'form': form,
			'user': request.user,
			'profile': request.user.profile
		}
	)