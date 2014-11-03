from django.conf.urls import include, url, patterns
from django.contrib import admin
import music
from music import urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'music_recommendation.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include(music.urls)),
]

