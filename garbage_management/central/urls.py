from django.urls import path
from .views import index, CarsView, CarDetailsView, TrashBinDetailsView, TrashBinsView, UsersView, UserDetailsView

urlpatterns = [
    path('', index, name="mainview"),
    path('cars/', CarsView.as_view(), name="cars"),
    path('cars/<int:pk>', CarDetailsView.as_view(), name="cars details"),
    path('trash-bins/', TrashBinsView.as_view(), name="cars"),
    path('trash-bins/<int:pk>', TrashBinDetailsView.as_view(), name="cars details"),
    path('users/', UsersView.as_view(), name="cars"),
    path('users/<int:pk>', UserDetailsView.as_view(), name="cars details"),
]
