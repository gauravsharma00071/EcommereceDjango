from django.db import models

# Create your models here.
class Contact(models.Model):
    #contact_id= models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    desc=models.TextField(max_length=600)
    phonenumber=models.IntegerField()

    def __str__(self):
        return self.name

class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=100)
    category=models.CharField(max_length=40, default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)

    image=models.ImageField(upload_to='shop/images',default="")

    def __str__(self):
        return self.product_name
