from django.urls import path
from .views import *
urlpatterns = [
    path("", index, name="index"),
    path("<int:id>", view_student, name="view_student"),
    path("add_student/", add_student, name="add_student"),
    path("edit_student/<int:id>", edit, name="edit_student"),
    path("delete_student/<int:id>", delete_student, name="delete_student"),
]
