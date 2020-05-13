from phone_tax import PhoneTax
from constant import COST_PHONE_CONNECTION

class CalculateFreeTax(PhoneTax):

  def calculate(self, record, start_date, end_date):
    return COST_PHONE_CONNECTION
