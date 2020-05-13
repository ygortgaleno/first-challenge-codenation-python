import abc

class PhoneTax(metaclass = abc.ABCMeta):

  @abc.abstractmethod
  def calculate(self):
    pass
