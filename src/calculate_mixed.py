from datetime import datetime
from math import floor as round_floor
from constant import COST_PER_MINUTE_EVENING, COST_PHONE_CONNECTION
from phone_tax import PhoneTax

class CalculateMixed(PhoneTax):

  def calculate(self, record, start_date, end_date):

    if end_date.hour >= 22:
      if(start_date.second <= end_date.second):
        new_end_date = datetime(end_date.year, end_date.month, end_date.day,
        22,0, start_date.second)
      else:
        new_end_date = datetime(end_date.year, end_date.month, end_date.day,
        22,0, 0)

      total = round(int(round_floor((new_end_date - start_date).seconds / 60))
      * COST_PER_MINUTE_EVENING + COST_PHONE_CONNECTION, 2)

    else:
      new_start_date = datetime(start_date.year, start_date.month,
      start_date.day, 6, 0, 0)

      total = round(int(round_floor((end_date - new_start_date).seconds / 60))
      * COST_PER_MINUTE_EVENING + COST_PHONE_CONNECTION, 2)

    return total
