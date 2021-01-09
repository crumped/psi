from django.urls import path
from .views import index, CarsView, CarDetailsView, TrashBinDetailsView, TrashBinsView, UsersView, UserDetailsView,\
    TrackView, TrackDetailsView, BinTrackView, BinTrackDetailsView, KeysView, KeysDetailsView, InvoicesView, \
    InvoicesDetailsView, InvoicesNamesView, InvoicesNamesDetailsView, ScheduleView, ScheduleDetailsView

urlpatterns = [
    path('', index, name="mainview"),
    path('cars/', CarsView.as_view(), name="cars"),
    path('cars/<int:pk>', CarDetailsView.as_view(), name="cars details"),
    path('trash-bins/', TrashBinsView.as_view(), name="trash-bins"),
    path('trash-bins/<int:pk>', TrashBinDetailsView.as_view(), name="trash-bins details"),
    path('users/', UsersView.as_view(), name="users"),
    path('users/<int:pk>', UserDetailsView.as_view(), name="users details"),
    path('tracks/', TrackView.as_view(), name="tracks"),
    path('tracks/<int:pk>', TrackDetailsView.as_view(), name="tracks details"),
    path('stops/', BinTrackView.as_view(), name="stops"),
    path('stops/<int:pk>', BinTrackDetailsView.as_view(), name="stops details"),
    path('keys/', KeysView.as_view(), name="keys"),
    path('keys/<int:pk>', KeysDetailsView.as_view(), name="keys details"),
    path('invoices/', InvoicesView.as_view(), name="invoices"),
    path('invoices/<int:pk>', InvoicesDetailsView.as_view(), name="invoices details"),
    path('invoices-names/', InvoicesNamesView.as_view(), name="invoices names"),
    path('invoices-names/<int:pk>', InvoicesNamesDetailsView.as_view(), name="invoices names details"),
    path('schedule/', ScheduleView.as_view(), name="schedule"),
    path('schedule/<int:pk>', ScheduleDetailsView.as_view(), name="schedule details"),
]
