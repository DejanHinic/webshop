from django.conf import settings
from django.db import models
from shop.models import Product
User = settings.AUTH_USER_MODEL


class CartManager(models.Manager):
	def new_or_get(self, request):
		cart_id = request.session.get("cart_id", None)
		ok = self.get_queryset().filter(id=cart_id)
		if ok.count() == 1:
			new_obj = False
			cart_obj = ok.first()
			if request.user.is_authenticated() and cart_obj.user is None:
				cart_obj.user = request.user
				cart_obj.save()
		else:
			cart_obj = Cart.objects.new(user=request.user)
			new_obj = True
			request.session['cart_id'] = cart_obj.id
			return cart_obj, new_obj

def new(request, user=None):
    user_obj = None
    if user is not None:
        if request.user.is_authenticated():
            user_obj = user
    return self.model.objects.create(user=user_obj)


class Cart(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    products = models.ManyToManyField(Product, blank=True)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

metal = CartManager()
objects = CartManager()


def __str__(self):
    return str(self.id)
