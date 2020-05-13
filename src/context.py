from phone_tax import PhoneTax
from datetime import datetime

class Context:
  def __init__(self, strategy: PhoneTax) -> None:
    self._strategy = strategy

  @property
  def strategy(self) -> PhoneTax:
    return self._strategy

  @strategy.setter
  def strategy(self, strategy: PhoneTax) -> None:
    self._strategy = strategy

  def calculate(self, record):
    start_date = datetime.fromtimestamp(record['start'])
    end_date = datetime.fromtimestamp(record['end'])

    return self._strategy.calculate(record, start_date, end_date)
