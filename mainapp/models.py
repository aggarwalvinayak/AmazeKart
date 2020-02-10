from django.db import models
from django.conf import settings
from django.db import models

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
		return str(str(self.productid) + " " + str(self.productname) )

class Image(models.Model):
	imageid=models.IntegerField()
	imageurl=models.URLField()
	product=models.ForeignKey(Product,on_delete=models.CASCADE)

	def __str__(self):
		return str(str(self.imageid) + " " +  str(self.imageurl) )
