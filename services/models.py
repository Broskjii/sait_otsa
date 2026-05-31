from django.db import models
from django.core.validators import RegexValidator


class ServiceRequest(models.Model):
    """Модель для хранения заявок от клиентов"""
    
    SERVICE_TYPES = (
        ('repair', 'Ремонт автомобилей'),
        ('cargo', 'Грузоперевозки'),
    )
    
    service_type = models.CharField(
        max_length=10, 
        choices=SERVICE_TYPES,
        verbose_name='Тип услуги'
    )
    name = models.CharField(max_length=100, verbose_name='Имя')
    
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Формат: '+999999999'. До 15 цифр."
    )
    phone = models.CharField(
        validators=[phone_regex], 
        max_length=17, 
        verbose_name='Телефон'
    )
    
    email = models.EmailField(blank=True, null=True, verbose_name='Email')
    message = models.TextField(verbose_name='Сообщение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_processed = models.BooleanField(default=False, verbose_name='Обработано')
    
    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.get_service_type_display()}"


class ContactInfo(models.Model):
    """Модель для контактной информации"""
    
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Email')
    address = models.CharField(max_length=200, verbose_name='Адрес', blank=True)
    work_hours = models.CharField(max_length=100, verbose_name='Часы работы')
    
    class Meta:
        verbose_name = 'Контактная информация'
        verbose_name_plural = 'Контактная информация'
    
    def __str__(self):
        return f"Контакты: {self.phone}"