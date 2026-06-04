import random
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactInfo, ServiceRequest
from .forms import ServiceRequestForm


def get_captcha(request):
    """Генерирует простой математический пример для капчи"""
    a = random.randint(2, 9)
    b = random.randint(1, 9)
    request.session['captcha_answer'] = a + b
    return f"{a} + {b}"


def home(request):
    """Главная страница"""
    contact = ContactInfo.objects.first()
    return render(request, 'services/home.html', {'contact': contact})


def auto_repair(request):
    """Страница ремонта автомобилей"""
    contact = ContactInfo.objects.first()
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
    
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        user_answer = request.POST.get('captcha', '').strip()
        correct_answer = str(request.session.get('captcha_answer', ''))
        
        if user_answer != correct_answer:
            messages.error(request, 'Неверный ответ на проверку. Попробуйте еще раз.')
        elif form.is_valid():
            service_request = form.save(commit=False)
            service_request.service_type = 'repair'
            service_request.save()
            messages.success(request, 'Ваша заявка успешно отправлена! Мы свяжемся с вами в ближайшее время.')
            return redirect('auto_repair')
    else:
        form = ServiceRequestForm(initial={'service_type': 'repair'})
    
    captcha_question = get_captcha(request)
    
    return render(request, 'services/auto_repair.html', {
        'contact': contact,
        'form': form,
        'services': services_list,
        'captcha_question': captcha_question
    })


def cargo_transport(request):
    """Страница грузоперевозок"""
    contact = ContactInfo.objects.first()
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
    
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        user_answer = request.POST.get('captcha', '').strip()
        correct_answer = str(request.session.get('captcha_answer', ''))
        
        if user_answer != correct_answer:
            messages.error(request, 'Неверный ответ на проверку. Попробуйте еще раз.')
        elif form.is_valid():
            service_request = form.save(commit=False)
            service_request.service_type = 'cargo'
            service_request.save()
            messages.success(request, 'Ваша заявка успешно отправлена! Мы свяжемся с вами в ближайшее время.')
            return redirect('cargo_transport')
    else:
        form = ServiceRequestForm(initial={'service_type': 'cargo'})
    
    captcha_question = get_captcha(request)
    
    return render(request, 'services/cargo_transport.html', {
        'contact': contact,
        'form': form,
        'services': services_list,
        'captcha_question': captcha_question
    })