from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactInfo, ServiceRequest
from .forms import ServiceRequestForm


def home(request):
    """Главная страница"""
    contact = ContactInfo.objects.first()
    return render(request, 'services/home.html', {'contact': contact})


def auto_repair(request):
    """Страница ремонта автомобилей"""
    contact = ContactInfo.objects.first()
    
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.service_type = 'repair'
            service_request.save()
            messages.success(request, 'Ваша заявка успешно отправлена! Мы свяжемся с вами в ближайшее время.')
            return redirect('auto_repair')
    else:
        form = ServiceRequestForm(initial={'service_type': 'repair'})
    
    services_list = [
        'Диагностика неисправностей',
        'Ремонт двигателя',
        'Ремонт ходовой части',
        'Замена масла и фильтров',
        'Ремонт тормозной системы',
        'Электрика и электроника',
        'Кузовной ремонт',
        'Шиномонтаж и балансировка',
    ]
    
    return render(request, 'services/auto_repair.html', {
        'contact': contact,
        'form': form,
        'services': services_list
    })


def cargo_transport(request):
    """Страница грузоперевозок"""
    contact = ContactInfo.objects.first()
    
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.service_type = 'cargo'
            service_request.save()
            messages.success(request, 'Ваша заявка успешно отправлена! Мы свяжемся с вами в ближайшее время.')
            return redirect('cargo_transport')
    else:
        form = ServiceRequestForm(initial={'service_type': 'cargo'})
    
    services_list = [
        'Перевозка грузов до 3,5 тонн',
        'Квартирные переезды',
        'Офисные переезды',
        'Доставка строительных материалов',
        'Доставка мебели',
        'Услуги грузчиков',
        'Междугородние перевозки',
        'Вывоз мусора',
    ]
    
    return render(request, 'services/cargo_transport.html', {
        'contact': contact,
        'form': form,
        'services': services_list
    })