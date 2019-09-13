from django.conf.urls import url
from shop.views.cart_view import cart, add_to_cart
from django.conf.urls.static import static
from gallery import settings

app_name = "shop"

urlpatterns = [
    url(r"^cart/$", cart, name="cart"),
    url(r"^add_to_cart/(?P<product_id>[0-9]+)/$", add_to_cart, name="add_to_cart")
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
