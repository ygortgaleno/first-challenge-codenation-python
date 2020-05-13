from datetime import datetime
from collections import Counter
from context import Context
from calculate_mixed import CalculateMixed
from calculate_normal_tax import CalculateNormalTax
from calculate_free_tax import CalculateFreeTax

records = [
    {'source': '48-996355555', 'destination': '48-666666666', 'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097', 'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097', 'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788', 'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788', 'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099', 'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697', 'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099', 'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697', 'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097', 'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564627800, 'start': 1564626000}
]

def format_records(records):
  records_formated = {}
  for record in records:
    records_formated[record['source']] = []

  for record in records:
    records_formated[record['source']].append({
      'start': record['start'],
      'end': record['end']
    })
    
  return records_formated

def classify_by_phone_number(records):
  results = []
  context = None
  records_formated = format_records(records)
  concrate_calculate_mixed = CalculateMixed()
  concrate_calculate_normal_tax = CalculateNormalTax()
  concrate_calculate_free_tax = CalculateFreeTax()

  for key, values in records_formated.items():
    tmp_dict = {
      'source': key,
      'totals': []
    }

    for value in values:
      date_converted_start = datetime.fromtimestamp(value['start'])
      date_converted_end = datetime.fromtimestamp(value['end'])

      if ((6 <= date_converted_start.hour < 22) and
      (6 <= date_converted_end.hour < 22)):
        context = Context(concrate_calculate_normal_tax)

      elif ((date_converted_start.hour >= 22 and date_converted_end.hour >= 22)
      or (date_converted_start.hour < 6 and date_converted_end.hour < 6)):
        context = Context(concrate_calculate_free_tax)

      else:
        context = Context(concrate_calculate_mixed)

      tmp_dict['totals'].append(context.calculate(value))

    results.append({
      'source': tmp_dict['source'],
      'total': round(sum(tmp_dict['totals']),2)
    })

  results = sorted(results, key=lambda each_call: each_call['total'],
  reverse=True)

  print(results)
  return results

if __name__ == "__main__":
  classify_by_phone_number(records)
