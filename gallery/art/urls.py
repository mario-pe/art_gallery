from django.conf.urls import url
from art.views import author_views, category_views, product_views

from art.views.author_views import authors, author_details

app_name = 'care_point'

urlpatterns = [
    url(r'^$', category_views.index, name='index'),

    url(r'^authors/$', authors, name='authors'),
    url(r'^authors/(?P<author_id>[0-9]+)/$', author_details, name='author_details')

]