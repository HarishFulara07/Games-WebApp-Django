"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from JSGames.views import home
from JSGames.views import games
from JSGames.views import game2048
from JSGames.views import gamebingohome
from JSGames.views import gamebingoplay
from JSGames.views import gamebuttonmania
from JSGames.views import gamebatshoot
from JSGames.views import gamebrickbreaker
from JSGames.views import gametigerjump

urlpatterns = [
	url(r'^$', home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^games/$', games, name='games'),
    url(r'^game2048/$', game2048, name='game2048'),
    url(r'^gamebingohome/$', gamebingohome, name='gamebingohome'),
    url(r'^gamebingoplay/$', gamebingoplay, name='gamebingoplay'),
    url(r'^gamebuttonmania/$', gamebuttonmania, name='gamebuttonmania'),
    url(r'^gamebatshoot/$', gamebatshoot, name='gamebatshoot'),
    url(r'^gamebrickbreaker/$', gamebrickbreaker, name='gamebrickbreaker'),
    url(r'^gametigerjump/$', gametigerjump, name='gametigerjump'),
]

"""
* The method which we are using to access our static files is unsecure and is recommended
only for development purposes. It is not recommended for production.

* Also, we have a DEBUG field in our setings file which is set to True.
This DEBUG field should be set to true if we are in development mode.

* So, we can combine these two together to access our static files in development mode.
"""

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
else:
    urlpatterns += url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),