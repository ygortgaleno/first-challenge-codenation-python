from math import floor as round_floor
from phone_tax import PhoneTax
from constant import COST_PER_MINUTE_EVENING, COST_PHONE_CONNECTION

class CalculateNormalTax(PhoneTax):

  def calculate(self, record, start_date, end_date):
    total = round(int(round_floor((end_date - start_date).seconds / 60))
      * COST_PER_MINUTE_EVENING + COST_PHONE_CONNECTION, 2)

    return total
