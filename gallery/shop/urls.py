from django.conf.urls import url
from shop.views.cart_view import cart, add_to_cart, remove_from_cart
from shop.views.address_view import add_address
from shop.views.order_view import confirm_order, make_no_logged_user_order, make_logged_user_order, order_details, user_order_history
from django.conf.urls.static import static
from gallery import settings

app_name = "shop"

urlpatterns = [
    url(r"^cart/$", cart, name="cart"),
    url(r"^add_to_cart/(?P<product_id>[0-9]+)/$", add_to_cart, name="add_to_cart"),
    url(r"^remove_from_cart/(?P<product_id>[0-9]+)/$", remove_from_cart, name="remove_from_cart"),
    url(r"^confirm_order/$", confirm_order, name="confirm_order"),
    url(r"^make_no_logged_user_order/$", make_no_logged_user_order, name="make_no_logged_user_order"),
    url(r"^make_logged_user_order/$", make_logged_user_order, name="make_logged_user_order"),
    url(r"^add_address/$", add_address, name="add_address"),
    url(r"^order_details/(?P<order_id>[0-9]+)/$", order_details, name="order_details"),
    url(r"^user_order_history/$", user_order_history, name="user_order_history"),
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
