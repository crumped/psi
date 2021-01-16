from django.urls import path
from .views import index, TrashBinDetail, TrashBinList, UserDetailsView, TrackList, TrackDetail,\
    BinTrackList, BinTrackDetail, KeysList, KeysDetail, InvoicesList, InvoicesDetail, \
    InvoicesNamesList, InvoicesNamesDetail, ScheduleList, ScheduleDetail, CarList, CarDetail, \
    UserList, GarbageDumpList, GarbageDumpDetail

urlpatterns = [
    path('', index, name="mainview"),
    path('cars', CarList.as_view(), name=CarList.name),
    path('cars/<int:pk>', CarDetail.as_view(), name=CarDetail.name),

    path('trash-bins', TrashBinList.as_view(), name=TrashBinList.name),
    path('trash-bins/<int:pk>', TrashBinDetail.as_view(), name=TrashBinDetail.name),

    path('users', UserList.as_view(), name=UserList.name),
    path('users/<int:pk>', UserDetailsView.as_view(), name="users details"),

    path('tracks', TrackList.as_view(), name=TrackList.name),
    path('tracks/<int:pk>', TrackDetail.as_view(), name=TrackDetail.name),

    path('stops', BinTrackList.as_view(), name=BinTrackList.name),
    path('stops/<int:pk>', BinTrackDetail.as_view(), name=BinTrackDetail.name),

    path('keys', KeysList.as_view(), name=KeysList.name),
    path('keys/<int:pk>', KeysDetail.as_view(), name=KeysDetail.name),

    path('invoices', InvoicesList.as_view(), name=InvoicesList.name),
    path('invoices/<int:pk>', InvoicesDetail.as_view(), name=InvoicesDetail.name),

    path('invoices-names', InvoicesNamesList.as_view(), name=InvoicesNamesList.name),
    path('invoices-names/<int:pk>', InvoicesNamesDetail.as_view(), name=InvoicesNamesDetail.name),

    path('schedule', ScheduleList.as_view(), name=ScheduleList.name),
    path('schedule/<int:pk>', ScheduleDetail.as_view(), name=ScheduleDetail.name),

    path('places', GarbageDumpList.as_view(), name=GarbageDumpList.name),
    path('places/<int:pk>', GarbageDumpDetail.as_view(), name=GarbageDumpDetail.name),
]
