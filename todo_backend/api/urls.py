from django.urls import path
from . import views



urlpatterns = [
    path('message' , views.api_message ),
    path('get-all-todo' , views.get_all_todo),
    path('add-todo' , views.add_todo),
    path('filter-category/<str:category>' , views.get_category),
    path('edit-view/<str:todo_id>' , views.edit_view),
    path('delete-todo/<str:todo_id>' , views.delete_todo),
    path('search' , views.search_todo)
]
