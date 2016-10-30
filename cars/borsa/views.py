from django.shortcuts import render
from django.views.generic.detail import DetailView
from .forms import CarForm
from .models import Car, CarImage
from django.shortcuts import redirect, get_object_or_404

# Create your views here.

def car_list(request):
    cars = Car.objects.all()
    mainphoto = CarImage.objects.all()[0]
    return render(request, 'borsa/car_list.html', {'cars': cars, 'mainphoto': mainphoto})
	
class CarDetailView(DetailView):

    model = Car

    def get_context_data(self, **kwargs):
        context = super(CarDetailView, self).get_context_data(**kwargs)
        return context


def car_new(request):
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.save()
            return redirect('car_detail', pk=car.pk)
    else:
        form = CarForm()
    return render(request, 'borsa/car_new.html', {'form': form})


def car_edit(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == "POST":
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            car = form.save(commit=False)
            car.save()
            return redirect('car_detail', pk=car.pk)
    else:
        form = CarForm(instance=car)
    return render(request, 'borsa/car_edit.html', {'form': form})
    

def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'borsa/car_detail.html', {'car': car})
