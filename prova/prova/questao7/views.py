from django.shortcuts import render

# Create your views here.
from .forms import MarkerForm
from .models import Marker
from django.http import HttpResponse, JsonResponse

def questa7DeleteMarker(request):
    if request.method == "POST":
        id = request.POST.get("id")
        #se fosse ligar ao usuario atual filtrar para ver se tem direito
        #ex .filter(user=request.user,.....)
        try:
            marker = Marker.objects.get(id=id)
            marker.delete()
            return HttpResponse("sucesso")
        except Exception as e:
            return HttpResponse("erro")


def questao7Update(request):
    print("atualizando")
    if request.method=="GET":
        markers = Marker.objects.all()
        form = MarkerForm(prefix="marker_form")
        edit_form = MarkerForm(prefix="marker_edit_form")
        context = {
            "markers": markers,
            'marker_form': form,
            'edit_form': edit_form,
        }
        return render(request, "questao7/questao7.html", context=context)
    if request.method=="POST":
        form = MarkerForm(prefix="marker_form")
        edit_form = MarkerForm(request.POST or None,prefix="marker_edit_form")

        if edit_form.is_valid():
            print("valido")
            edit_form.update()
            edit_form = MarkerForm(prefix="marker_edit_form")
        else:
            print("invalido")
            print("erros "+str(form.errors))
        markers = Marker.objects.all()
        context = {
            "markers": markers,
            'marker_form': form,
            'edit_form': edit_form,
        }
        return render(request, "questao7/questao7.html", context=context)


def questao7(request):
    if request.method=="GET":
        markers = Marker.objects.all()
        form = MarkerForm( prefix="marker_form")
        edit_form = MarkerForm(prefix="marker_edit_form")
        context = {
            "markers": markers,
            'marker_form': form,
            'edit_form':edit_form,
        }
        return render(request, "questao7/questao7.html", context=context)
    if request.method=="POST":
        markers = Marker.objects.all()
        form = MarkerForm(request.POST or None, prefix="marker_form")

        if form.is_valid():
            form.save()
            form = MarkerForm( prefix="marker_form")
        else:
            print("invalido "+str(form.errors))
        edit_form = MarkerForm(prefix="marker_edit_form")

        context = {
            "markers": markers,
            'marker_form': form,
            'edit_form': edit_form,
        }
        return render(request, "questao7/questao7.html", context=context)