from django.shortcuts import render
from homeland_manager.db_modules import db_direct
from homeland_manager.models import Apartment, Owner, CommonDue, ElevatorDue, MonthlyDue, PaymentDate

def format_decimals(data):
    decimal = f'{data:.2f}'
    return decimal

# Create your views here.
def index(request):
    """View function for home page of site."""
    
    '''
    value = <model_name>.objects.filter(<table_column>=<value>).values_list(<table_column>)
    Then 'value' will be object of type List and will contain as elements all table-rows that match the filtering
    Extracted 'value' list-element will be object of type Tuple that will contain all column-values for the row
    A table-cell object can be obtained either by extracting the proper values_list() option or by the second <value> index
    '''

    # Get the latest date, date model would return the latest record first
    date_record = PaymentDate.objects.filter().values_list()[1]
    tax_date_index = date_record[0]
    last_date = date_record[1]

    # Create data type objects
    common_data_list = ['cleaner_tax', 'stairs_electricity', 'other_payments', 'other_comment']
    elevator_data_list = ['elevator_tax', 'elevator_electricity', 'elevator_additional', 'elevator_comment']

    # Get DB data for the created objects
    common_data_dict = {}
    for i in common_data_list:
        common_data_dict[i] = CommonDue.objects.filter(tax_date=tax_date_index).values_list(f'{i}')[0][0]
    elevator_data_dict = {}
    for i in elevator_data_list:
        elevator_data_dict[i] = ElevatorDue.objects.filter(bill_date=tax_date_index).values_list(f'{i}')[0][0]

    # Calculate due amounts
    total_common_sum = common_data_dict['cleaner_tax'] + common_data_dict['stairs_electricity'] + common_data_dict['other_payments']
    total_elevator_sum = elevator_data_dict['elevator_tax'] + elevator_data_dict['elevator_electricity'] + elevator_data_dict['elevator_additional']
    first_floor_apartments = total_common_sum / 8
    elevator_apartments = (total_elevator_sum / 6) + (total_common_sum / 8)
    
    # Format the calculations
    total_common_sum = format_decimals(total_common_sum)
    total_elevator_sum = format_decimals(total_elevator_sum)
    first_floor_apartments = format_decimals(first_floor_apartments)
    elevator_apartments = format_decimals(elevator_apartments)

    # Build page data stream
    home_data = {
        'last_date': last_date,
        'cleaner_tax': common_data_dict['cleaner_tax'],
        'stairs_electricity': common_data_dict['stairs_electricity'],
        'other_common': common_data_dict['other_payments'],
        'other_comment': common_data_dict['other_comment'],
        'elevator_tax': elevator_data_dict['elevator_tax'],
        'elevator_electricity': elevator_data_dict['elevator_electricity'],
        'other_elevator': elevator_data_dict['elevator_additional'],
        'elevator_comment': elevator_data_dict['elevator_comment'],
        'total_common_sum': total_common_sum,
        'total_elevator_sum': total_elevator_sum,
        'first_floor_apartments': first_floor_apartments,
        'elevator_apartments': elevator_apartments,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=home_data)
