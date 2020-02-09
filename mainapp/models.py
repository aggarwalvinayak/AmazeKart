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

# class ProductImg(models.Model): 
#     Productimg = models.ImageField(upload_to='images/') 

# class Document(models.Model):
#   file = models.FileField('Document', upload_to='image/')

#   @property
#   def filename(self):
#      name = self.file.name.split("/")[1].replace('_',' ').replace('-',' ')
#      return name
#   def get_absolute_url(self):
#      return reverse('myapp:document-detail', kwargs={'pk': self.pk})

class Photo(models.Model):
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)