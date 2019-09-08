from django.conf.urls import url
from shop.views.cart_view import cart, add_to_cart

app_name = "care_point"

urlpatterns = [
    url(r"^cart/(?P<product_id>[0-9]+)/$", add_to_cart, name="add_to_cart"),
]
