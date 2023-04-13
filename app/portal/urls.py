"""URLs for job API"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from portal import views
from . import views

# `DefaultRouter` provided by DRF automatically creates URL routing for us
# TODO - Refer
# https://www.django-rest-framework.org/api-guide/routers/#defaultrouter

router = DefaultRouter()

# this app name will be utilized in reverse function
app_name = "Portal"
router.register("portals", views.PortalViewSet)
urlpatterns = [
    path("", include(router.urls)),
    # path("portal/", views.PortalViewSet.as_view(), name="portal"),
    # path("portalcrud/<int:id>/", views.PortalViewSetCRUD.as_view(), name="portalcrud"),
]
