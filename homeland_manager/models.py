from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique monthly_bills instances

# Create your models here.
class PaymentDate(models.Model):
    """ Model representing an apartment. """
    dates = models.DateField()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        """ String for representing the Model object. """
        return f'{self.dates}'

class Apartment(models.Model):
    """ Model representing an apartment. """
    floor_num = models.IntegerField()
    apartment_num = models.IntegerField()
    common_due = models.CharField(max_length=5)
    elevator_due = models.CharField(max_length=5)

    class Meta:
        ordering = ['floor_num', 'apartment_num']

    def get_absolute_url(self):
        """ Returns the url to access a particular apartment instance. """
        return reverse('apartment-details', args=[str(self.id)])

    def __str__(self):
        """ String for representing the Model object. """
        return f'Floor {self.floor_num}, Apartment {self.apartment_num}'


class Owner(models.Model):
    """ Model representing an owner. """
    names = models.CharField(max_length=30)
    apartment = models.ForeignKey(Apartment, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        ordering = ['apartment', 'names']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.apartment}: {self.names}'
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this monthly_bills."""
        return reverse('owner-details', args=[str(self.id)])


class CommonDue(models.Model):
    """Model representing a monthly_bills (but not a specific copy of a monthly_bills)."""
    tax_date = models.ForeignKey(PaymentDate, on_delete=models.SET_NULL, null=True)
    cleaner_tax = models.IntegerField(null=True, blank=True)
    stairs_electricity = models.DecimalField(max_digits=5, decimal_places=2)
    other_payments = models.DecimalField(max_digits=5, decimal_places=2)
    other_comment = models.CharField(max_length=30, null=True, blank=True)    
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this monthly_bills."""
        return reverse('monthly-taxes', args=[str(self.id)])

    def __str__(self):
        """ String for representing the Model object. """
        return f'Common taxes for date: {self.tax_date}'


class ElevatorDue(models.Model):
    """Model representing a specific due of a monthly_bills."""
    bill_date = models.ForeignKey(PaymentDate, on_delete=models.SET_NULL, null=True)
    elevator_tax = models.IntegerField(null=True, blank=True)
    elevator_electricity = models.DecimalField(max_digits=5, decimal_places=2)
    elevator_additional = models.DecimalField(max_digits=5, decimal_places=2)
    elevator_comment = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        ordering = ['bill_date']

    def __str__(self):
        """ String for representing the Model object. """
        return f'Elevator taxes for date: {self.bill_date}'


class MonthlyDue(models.Model):
    """Model representing a specific due of a monthly_bills."""
    due_date = models.ForeignKey(PaymentDate, on_delete=models.SET_NULL, null=True)
    due_apartment = models.ForeignKey(Apartment, on_delete=models.SET_NULL, null=True)
    monthly_common = models.DecimalField(max_digits=5, decimal_places=2)
    monthly_elevator = models.DecimalField(max_digits=5, decimal_places=2)
    monthly_given = models.DecimalField(max_digits=5, decimal_places=2)
    
    DUE_STATUS = (
        ('a', 'Awaiting for payment'),
        ('m', 'Missed payment'),
        ('p', 'Payed'),
        ('s', 'Skip'),
    )

    status = models.CharField(
        max_length=1,
        choices=DUE_STATUS,
        blank=True,
        default='a',
        help_text='monthly bills information',
    )

    class Meta:
        ordering = ['due_date']

    def __str__(self):
        """ String for representing the Model object. """
        return f'{self.due_date}  {self.due_apartment} ({self.status})'