# Conversion from metric to imperial units

class MetricToImperial():
    def __init__(self):
        self.m_to_in = 39.3701
        self.m_to_ft = 3.28084
        
    def convert(self, value):
        return round((value * self.m_to_in), 5)
    
    def convert_feet(self, value):
        return round((value * self.m_to_ft), 5)
    
    def convert_meters(self, value):
        return round((value / self.m_to_in), 5)
    
    

logger = MetricToImperial()
print(logger.convert(1))
print(logger.convert_feet(1))
print(logger.convert_meters(1))

        
        