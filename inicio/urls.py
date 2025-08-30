from django.urls import path
from inicio.views import inicio, crear_computadora, listado_de_computadora, computadora_detalle, ComputadoraBorrar, ComputadoraActualizar
from inicio import views

urlpatterns = [
    path('', inicio, name='inicio'),
    path("acerca-de-mi/", views.acerca_de_mi, name="acerca_de_mi"),
    path('computadora/', listado_de_computadora, name='listado_de_computadora'),
    path('computadora/crear/', crear_computadora, name='crear_computadora'),
    path('computadora/<int:id_computadora>/', computadora_detalle, name='computadora_detalle'),
    path('computadora/<int:pk>/borrar/', ComputadoraBorrar.as_view(), name='computadora_borrar'),
    path('computadora/<int:pk>/actualizar/', ComputadoraActualizar.as_view(), name='computadora_actualizar'),
]