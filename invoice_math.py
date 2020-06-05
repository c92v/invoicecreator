from decimal import *

class InvoiceMath:
        def __init__(self):
                self.rate = 0.87
                self.total = 0
        def calculate_cost(self, time):
                getcontext().prec = 4
                return float(Decimal(time) * Decimal(self.rate))
        def format_time(self, time):
                minutes = time // 60
                seconds = time % 60
                if seconds >= 16 and seconds <= 45:
                        minutes += 0.5
                elif seconds >= 46 and seconds <= 59:
                        minutes += 1
                return minutes
        def convert_times(self, times):
                for key, value in times.items():
                        times[key] = [ self.format_time(value) ]
        def add_costs(self, times):
                for key, value in times.items():
                        value.append(self.calculate_cost(value[0]))
