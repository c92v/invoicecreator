from files import *
from invoice_math import *
from invoice_doc import *

Files = InvoiceFiles()
Calculations = InvoiceMath()
Document = InvoiceDocument()

data = Files.get_audio_information()
Calculations.convert_times(data)
Calculations.add_costs(data)

for k, v in data.items():
    print("File: {}\t Length: {}\t Cost: {}".format(k, v[0], v[1]))

print("Total:", Calculations.get_total())

Document.create_document(data)
