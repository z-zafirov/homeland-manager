from django.contrib import admin
from .models import Apartment, Owner, CommonDue, ElevatorDue, MonthlyDue, PaymentDate

# Register your models here.
admin.site.register(Apartment)
admin.site.register(Owner)
admin.site.register(CommonDue)
admin.site.register(ElevatorDue)
admin.site.register(MonthlyDue)
admin.site.register(PaymentDate)