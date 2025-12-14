from django.urls import path
from .views import DetalleTareaView

app_name = "tareas"

urlpatterns = [
    path("tarea/<uuid:pk>/", DetalleTareaView.as_view(), name="detalle_tarea"),
]
