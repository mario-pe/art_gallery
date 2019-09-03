from django.conf.urls import url

from art.views.index import index
from art.views.author_views import authors, author_details
from art.views.category_views import categories
from art.views.product_views import products

app_name = 'care_point'

urlpatterns = [
    url(r'^$', index, name='index'),

    url(r'^authors/$', authors, name='authors'),
    url(r'^authors/(?P<author_id>[0-9]+)/$', author_details, name='author_details'),
    url(r'^categories/$', categories, name='categories'),
    url(r'^product/$', products, name='product'),


]