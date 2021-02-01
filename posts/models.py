"""Posts models."""

# Django
"""from django.db import models

class User(models.Model):
	User model.

	email = models.EmailField(unique=True)
	password = models.CharField(max_length=100)

	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)

	is_admin = models.BooleanField(default=False)

	bio = models.TextField()

	birthdate = models.DateField(blank=True, null=True)

	country = models.CharField(max_length=100)
	city = models.CharField(default=None, max_length=100)

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)


	def __str__(self):
		Return email.
		return self.email"""

	
	

"""Posts models."""

# Django
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	"""Posts model."""

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)

	title = models.CharField(max_length=255)
	photo = models.ImageField(upload_to='posts/photos')

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		"""Return title and username."""
		return '{} by @{}'.format(self.title,self.user.username)