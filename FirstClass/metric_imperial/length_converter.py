class LengthConverter:
    def __init__(self, measure, system):
        """
        Constructor
        @param measure: The numeric measure to convert with up to two decimals
        @param system: The system of said measure ('metric' or 'imperial')
        """
        self.measure = round(measure, 2)
        self.system = system.lower()

    def convert(self):
        """
        Converts the measure to the other system.
        @return: The value of the conversion with up to two decimals
        """
        if self.system == 'metric':
            # Convert centimeters to inches
            converted = self.measure / 2.54
        elif self.system == 'imperial':
            # Convert inches to centimeters
            converted = self.measure * 2.54
        else:
            raise ValueError("Invalid system. Must be 'metric' or 'imperial'.")
        return round(converted, 2)