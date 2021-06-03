from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register('FilterClients', views.ClientFilterSet)
router.register('projects', views.ProjectViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('ClientDeleteByCountry/<area>/',views.ClientDeleteByCountry),
    path('DeleteClient/<id>/',views.delete_client),
    path('DeleteProject/<id>/',views.delete_project),
    path('ProjectDeleteByLanguage/<language>/',views.ProjectDeleteByLanguage),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh', TokenRefreshView.as_view()),
]
