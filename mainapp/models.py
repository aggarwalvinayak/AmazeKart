from django.db import models
from django.conf import settings
from django.db import models

# class AppUser(models.Model):
# 	username = models.CharField(max_length = 30)
# 	name = models.CharField(max_length = 100)
# 	email = models.EmailField()
# 	phoneno= models.CharField(max_length = 15)

# 	class Meta:
# 		verbose_name_plural='users'

# 	def __str__(self):
# 		return self.username

class Product(models.Model):
	productid = models.IntegerField()
	productname = models.CharField(max_length = 100)
	price = models.IntegerField()
	category = models.CharField(max_length = 100)
	user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
	description = models.TextField()

	def __str__(self):
		return self.productid

class Image(models.Model):
	imageid=models.IntegerField()
	imageurl=models.URLField()
	product=models.ForeignKey(Product,on_delete=models.CASCADE)

	def __str__(self):
		return self.imageid