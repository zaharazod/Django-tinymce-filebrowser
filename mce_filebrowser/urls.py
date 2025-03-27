from django.urls import path

from mce_filebrowser import views


urlpatterns = [
    path(
        r"^image/$",
        views.filebrowser,
        kwargs={"file_type": "img"},
        name="mce-filebrowser-images",
    ),
    path(
        r"^file/$",
        views.filebrowser,
        kwargs={"file_type": "doc"},
        name="mce-filebrowser-documents",
    ),
    path(
        r"^image/remove/(?P<item_id>\d+)/$",
        views.filebrowser_remove_file,
        kwargs={"file_type": "img"},
        name="mce-filebrowser-remove-image",
    ),
    path(
        r"^file/remove/(?P<item_id>\d+)/$",
        views.filebrowser_remove_file,
        kwargs={"file_type": "doc"},
        name="mce-filebrowser-remove-document",
    ),
]
