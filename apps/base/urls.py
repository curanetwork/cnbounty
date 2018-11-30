"""urlconf for the base application"""

from django.urls import include, path

from rest_framework import routers

from base import views


router = routers.DefaultRouter()
router.register(r'hunts', views.HuntViewSet, 'hunts')
router.register(r'bounties', views.BountyViewSet, 'bounties')
router.register(r'reports', views.ReportViewSet, 'reports')


urlpatterns = [
	path('', include(router.urls)),
	path('auth/', include('djoser.urls')),
	path('auth/', include('djoser.urls.jwt'))
]
