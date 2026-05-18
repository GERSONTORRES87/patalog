from django.urls import path
from . import views

app_name = 'mascotas'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('mascotas/', views.MascotaListView.as_view(), name='lista'),
    path('mascotas/<int:pk>/', views.MascotaDetailView.as_view(), name='detalle'),
    path('mascotas/nueva/', views.MascotaCreateView.as_view(), name='crear'),
    path('mascotas/<int:pk>/editar/', views.MascotaUpdateView.as_view(), name='editar'),
    path('mascotas/<int:pk>/eliminar/', views.MascotaDeleteView.as_view(), name='eliminar'),
    path('mascotas/<int:pk>/vacuna/', views.agregar_vacuna, name='agregar_vacuna'),
    path('vacuna/<int:pk>/eliminar/', views.eliminar_vacuna, name='eliminar_vacuna'),
]
