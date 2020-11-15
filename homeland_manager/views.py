from django.shortcuts import render
from homeland_manager.db_modules import db_direct
from homeland_manager.models import Apartment, Owner, CommonDue, ElevatorDue, MonthlyDue, PaymentDate

def cleanup(data):
    for d in data:
        str(d).replace(',','.')
        str(d).replace("'","")
        if isinstance(d, int) == True:
            return int(d)
        elif isinstance(d, float) == True:
            return float(d)
        else:
            if len(str(d)) < 1:
                return 0
            else:
                return d

def format_decimals(data):
    decimal = f'{data:.2f}'
    return decimal

# Create your views here.
def index(request):
    """View function for home page of site."""
    '''
    db_conn = db_extract.DBconnetcion()

    common_dues = db_conn.get_common_dues_for_date('2020-10-03')
    elevator_dues = db_conn.get_elevator_dues_for_date('2020-10-03')

    db_conn.close_db_connection()
    '''

    tax_date = 9

    # Create data type objects
    home_data = {}
    common_data_dict = {}
    elevator_data_dict = {}
    common_data_list = ['cleaner_tax', 'stairs_electricity', 'other_payments', 'other_comment']
    elevator_data_list = ['elevator_tax', 'elevator_electricity', 'elevator_additional', 'elevator_comment']
    
    # Get DB data for the created ada objects
    for i in common_data_list:
        common_data_dict[i] = CommonDue.objects.filter(tax_date=tax_date).values_list(f'{i}')[0]
    for i in elevator_data_list:
        elevator_data_dict[i] = ElevatorDue.objects.filter(bill_date=tax_date).values_list(f'{i}')[0]
    
    # Clean up the DB data
    for k in common_data_dict.keys():
        common_data_dict[k] = cleanup(common_data_dict[k])
    for k in elevator_data_dict.keys():
        elevator_data_dict[k] = cleanup(elevator_data_dict[k])
    
    # Calculate due amounts
    total_common_sum = (common_data_dict['cleaner_tax'] + common_data_dict['stairs_electricity'] + common_data_dict['other_payments']) / 8
    total_elevator_sum = ((elevator_data_dict['elevator_tax'] + elevator_data_dict['elevator_electricity'] + elevator_data_dict['elevator_additional']) / 6) + total_common_sum
    
    # Format the calculations
    total_common_sum = format_decimals(total_common_sum)
    total_elevator_sum = format_decimals(total_elevator_sum)

    # Build page data stream
    home_data = {
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
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=home_data)