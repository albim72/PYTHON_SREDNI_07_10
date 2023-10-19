from oldresistance import OldResistor
from resistor import Resistor

r0 = OldResistor(10.2E2)
print(f"______________ klasa {r0.__class__.__name__} ________________")
print(r0)
print(r0.get_ohms())
r0.set_ohms(3.33E3)
print(r0.get_ohms())


r1 = Resistor(45.99E2)
print(f"______________ klasa {r1.__class__.__name__} ________________")
print(r1.ohms)
r1.ohms = 5.5E3
print(r1.ohms)
print(f'układ eleketryczny:\n'
      f'oporność: {r1.ohms} omów\n'
      f'napięcie prądu: {r1.voltage} V\n'
      f'natężenie prądu: {r1.current} A\n')
