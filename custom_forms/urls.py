from django.urls import path
from .views import (
                        ListCreateFormShape,
                        DeleteUpdateFormitem
                    )
urlpatterns=[
    path("", ListCreateFormShape.as_view(),name="list-items"),
    path("<int:pk>/",DeleteUpdateFormitem.as_view(),name="manage-item")
]