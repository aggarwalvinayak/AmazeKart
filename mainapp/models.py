from django.db import models
from django.conf import settings
from django.db import models

class Product(models.Model):
	productname = models.CharField(max_length = 100)
	price = models.IntegerField()
	category = models.CharField(max_length = 100)
	user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
	description = models.TextField()



	def __str__(self):
		return str(str(self.id) + " " + str(self.productname) )

class Image(models.Model):
	imageurl=models.URLField()
	product=models.ForeignKey(Product,on_delete=models.CASCADE)

	def __str__(self):
		return str(str(self.id) + " " +  str(self.imageurl) )
