import json
from datetime import datetime

FILEPATH = 'json/'
MONTHS = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

def get_critter(filename:str, critter_name:str, hemisphere:str):
    critter_name = critter_name.strip().lower().replace(' ','').replace('-','')
    with open(f'{FILEPATH}/{filename}.json', 'r') as f:
        data = json.load(f)
    if critter_name in data:
        return data[critter_name]
    else:
        return None


def get_monthly_critters(filename:str, hemisphere:str, month_period:int=-1):
    month = MONTHS[datetime.now().month+month_period]
    prev_month = MONTHS[datetime.now().month-1+month_period]
    
    with open(f'{FILEPATH}/{filename}.json', 'r') as f:
        data = json.load(f)

    monthly_critters = [critter for _, critter in data.items() if month in critter['months_available'][hemisphere]]
    new_critters = [critter for critter in monthly_critters if prev_month not in critter['months_available'][hemisphere]]
    recurring_critters = [critter for critter in monthly_critters if critter not in new_critters]

    return {'prev_month': prev_month, 'month': month, 'recurring_critters': recurring_critters, 'new_critters': new_critters}
