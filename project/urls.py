from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from accounts import views as acc_view
from service import views as serv_view

acc_router = DefaultRouter()
acc_router.register('register', acc_view.ProfileRegisterAPIView)

serv_router = DefaultRouter()
serv_router.register('taxi', serv_view.TaxiViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('auth/token/', obtain_auth_token),

    path('api/accounts/', acc_view.ProfileListAPIView.as_view()),
    path('account/<int:pk>/', acc_view.ProfileRetrieveUpdateDestroyAPIView.as_view()),

    # path('account/status', serv_view.StatusTypeCreateAPIView.as_view()),
    path('api/account/raiting/<id>/', serv_view.StatusTypeRetrieveUpdateDestroy.as_view()),

    path('api/service/taxi/<int:taxi_id>/order/', serv_view.OrderListCreateAPIView.as_view()),
    path('api/service/taxi/<int:taxi_id>/order/<int:pk>/', serv_view.OrderRetrieveUpdateDestroy.as_view()),

    path('api/account/', include(acc_router.urls)),
    path('api/service/', include(serv_router.urls)),
]