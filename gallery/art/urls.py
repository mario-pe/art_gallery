from django.conf.urls import url

from art.views.index import index
from art.views.author_views import authors, author_details
from art.views.category_views import categories, category_products
from art.views.product_views import products, product_details
from django.conf.urls.static import static

from gallery import settings

app_name = "care_point"

urlpatterns = [
    url(r"^$", index, name="index"),
    url(r"^authors/$", authors, name="authors"),
    url(r"^authors/(?P<author_id>[0-9]+)/$", author_details, name="author_details"),
    url(r"^categories/$", categories, name="categories"),
    url(
        r"^category/(?P<category_id>[0-9]+)/$",
        category_products,
        name="category_products",
    ),
    url(r"^products/$", products, name="products"),
    url(r"^product/(?P<product_id>[0-9]+)/$", product_details, name="product_details"),
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)