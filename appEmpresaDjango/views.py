from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Departamento, Habilidad, Empleado

#devuelve el listado de empresas
def index(request):
	departamentos = get_list_or_404(Departamento.objects.order_by('nombre'))
	context = {'lista_departamentos': departamentos }
	return render(request, 'index.html', context)

#devuelve los datos de un departamento
def detail(request, departamento_id):
	departamento = get_object_or_404(Departamento, pk=departamento_id)
	context = {'departamento': departamento }
	return render(request, 'detail.html', context)

class DepartamentoListView(ListView):
	model = Departamento
	template_name ="index.html"
	queryset = Departamento.objects.order_by('nombre');
	context_object_name = "lista_departamentos"
	def get_context_data(self,**kwargs):
		context = super(DepartamentoListView,self).get_context_data(**kwargs)
		context['subtitulo'] = "titulo pagina"
		return context

#devuelve los empelados de un departamento
def empleados(request, departamento_id):
	departamento = get_object_or_404(Departamento, pk=departamento_id)
	empleados =  departamento.empleado_set.all()
	context = {'departamento': departamento, 'empleados' : empleados }
	return render(request, 'empleados.html', context)

#devuelve los detalles de un empleado
#def empleado(request, empleado_id):
#	empleado = get_object_or_404(Empleado, pk=empleado_id)
#	habilidades =  empleado.habilidades.all()
#	context = { 'empleado': empleado, 'habilidades' : habilidades }
#	return render(request, 'empleado.html', context)
class EmpleadoDetailView(DetailView):
	model = Empleado
	template_name ='empleado.html'
	def get_context_data(self, **kwargs):
		context = super(EmpleadoDetailView,self).get_context_data(**kwargs)
		context['titulo'] = "detalles del empleado"
		return context

# Devuelve los detalles de una habilidad
def habilidad(request, habilidad_id):
    habilidad = get_object_or_404(Habilidad, pk=habilidad_id)
    empleados =  habilidad.empleado_set.all()
    context = { 'empleados': empleados, 'habilidad' : habilidad }
    return render(request, 'habilidad.html', context)