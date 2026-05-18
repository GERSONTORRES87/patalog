from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from datetime import date

from .models import Mascota, Vacuna, RegistroVacuna
from .forms import MascotaForm, RegistroVacunaForm


# ──────────────── INICIO ────────────────
def inicio(request):
    total_mascotas = Mascota.objects.count()
    total_vacunas = RegistroVacuna.objects.count()
    proximas = RegistroVacuna.objects.filter(
        proxima_dosis__gte=date.today()
    ).order_by('proxima_dosis')[:5]
    mascotas_recientes = Mascota.objects.order_by('-creado')[:4]
    return render(request, 'mascotas/inicio.html', {
        'total_mascotas': total_mascotas,
        'total_vacunas': total_vacunas,
        'proximas': proximas,
        'mascotas_recientes': mascotas_recientes,
    })


# ──────────────── MASCOTAS ────────────────
class MascotaListView(generic.ListView):
    model = Mascota
    template_name = 'mascotas/mascota_list.html'
    context_object_name = 'mascotas'


class MascotaDetailView(generic.DetailView):
    model = Mascota
    template_name = 'mascotas/mascota_detail.html'
    context_object_name = 'mascota'


class MascotaCreateView(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascotas/mascota_form.html'
    success_url = reverse_lazy('mascotas:lista')

    def form_valid(self, form):
        messages.success(self.request, 'Mascota registrada exitosamente.')
        return super().form_valid(form)


class MascotaUpdateView(UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascotas/mascota_form.html'

    def get_success_url(self):
        return reverse_lazy('mascotas:detalle', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        messages.success(self.request, 'Mascota actualizada exitosamente.')
        return super().form_valid(form)


class MascotaDeleteView(DeleteView):
    model = Mascota
    template_name = 'mascotas/mascota_confirm_delete.html'
    success_url = reverse_lazy('mascotas:lista')

    def form_valid(self, form):
        messages.success(self.request, 'Mascota eliminada.')
        return super().form_valid(form)


# ──────────────── VACUNAS ────────────────
def agregar_vacuna(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    if request.method == 'POST':
        form = RegistroVacunaForm(request.POST)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.mascota = mascota
            registro.save()
            messages.success(request, 'Vacuna registrada exitosamente.')
            return redirect('mascotas:detalle', pk=mascota.pk)
    else:
        form = RegistroVacunaForm()
    return render(request, 'mascotas/vacuna_form.html', {'form': form, 'mascota': mascota})


def eliminar_vacuna(request, pk):
    registro = get_object_or_404(RegistroVacuna, pk=pk)
    mascota_pk = registro.mascota.pk
    if request.method == 'POST':
        registro.delete()
        messages.success(request, 'Registro de vacuna eliminado.')
        return redirect('mascotas:detalle', pk=mascota_pk)
    return render(request, 'mascotas/vacuna_confirm_delete.html', {'registro': registro})
