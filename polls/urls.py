from django.urls import path,include
from .import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register('question',views.ViewApi)

urlpatterns = [
    path('api/',include(router.urls)),
    path('',views.index,name="index"),
    path('<int:question_id>/',views.detail,name="detail"),
    path('<int:question_id>/results/',views.results,name="results"),
    path('<int:question_id>/vote/',views.vote,name="vote"),
]