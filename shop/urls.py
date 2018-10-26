from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from .views import product_list, product_detail, signup, verify_form

# using the category and product slugs here for SEO purposes only

app_name = 'shop'
urlpatterns = [
    url(r'login$',
        LoginView.as_view(template_name='shop/login_form.html'),
        name='login'),
    url(r'logout$',
        LogoutView.as_view(),
        name='logout'),
    # the url for all ajax form validation requests
    url(r'^verify-form/(?P<product_id>[-\w]+)/', verify_form, name='verify_form'),
    url(r'^(?P<category_slug>[-\w]+)/$',
        product_list,
        name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        product_detail,
        name='product_detail'),
    url(r'signup$', signup, name='signup'),
    url(r'^$', product_list, name='product_list'),
]

