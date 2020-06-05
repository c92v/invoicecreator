from files import *
from invoice_math import *

Files = InvoiceFiles()
Calculations = InvoiceMath()

data = Files.get_audio_information()
Calculations.convert_times(data)
Calculations.add_costs(data)
print(data)
