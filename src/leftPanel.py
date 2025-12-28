

def assigner():
  min_price, max_price = input("Enter min and max price (e.g. 500 1500): ").split()
  min_bed, max_bed = input("Enter min and max bedroom count (e.g., 1, 2)").split()

  optionsDict = {
    "1" : "cats ok",
    "2" : "dogs ok",
    "3" : "furnished",
    "4" : "no smoking",
    "5" : "wheelchair accessible",
    "6" : "air conditiong",
    "7" : "EV charging",
    "8" : "no application fee",
    "9" : "no broker fee"
  }
  for x, y in optionsDict.items():
    print(f"[{x}]: {y}")

  choices = []
  choices = input("Enter numbers that you want checked (e.g, 1 2 5 6): ").split()
  selected = [optionsDict[x] for x in choices if x in optionsDict]

  return min_price, max_price, min_bed, max_bed, selected

  