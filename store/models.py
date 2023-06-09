from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# --------------------------------- Customer / user model
class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.name


# --------------------------------- Category model
class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories' 

    def __str__(self):
        return self.name


    # def get_absolute_url(self):
    #     return reverse('category-list', args=[self.slug])  


# --------------------------------- Products model
class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    digital = models.BooleanField(default=False,null=True, blank=True)
    description = models.TextField(max_length=250, blank=True)
    slug = models.SlugField(max_length=255)
    image = models.ImageField(upload_to='media/')
    
    class Meta:
        verbose_name_plural = 'products' 

    def __str__(self):
        return self.name  


   

# --------------------------------- General order model
class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)
		

# ---------------------------------Order of each item model
class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

# --------------------------------- Shipping model
class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	county = models.CharField(max_length=200, null=False)
	eircode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address

# ---------------------------------Review model
class Comment(models.Model):
    name = models.CharField(max_length=50)
    product = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, blank=True)
    comment = models.TextField(max_length=150, blank=True)
    rate = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
        
        class CommentForm(models.Model):
            class Meta:
                model = Comment
                fields = ['subject', 'comment', 'rate']