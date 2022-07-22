from django.urls import re_url

from wagtailtrans.views.translation import TranslationView

app_name = 'wagtailtrans'

urlpatterns = [
    re_url(r'^(?P<instance_id>\d+)/add/(?P<language_code>[^/]+)/$', TranslationView.as_view(), name='add'),
]
