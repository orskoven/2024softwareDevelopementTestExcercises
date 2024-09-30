class TemperatureConverter:
    def __init__(self, measure, scale):
        """
        Constructor
        @param measure: The numeric measure to convert with up to two decimals
        @param scale: The temperature scale of said measure ('C', 'F', 'K')
        """
        self.measure = round(measure, 2)
        self.scale = scale.upper()

    def convert(self, target_scale):
        """
        Converts the temperature to the target scale.
        @param target_scale: The destination temperature scale ('C', 'F', 'K')
        @return: The value of the conversion with up to two decimals
        """
        target_scale = target_scale.upper()
        conversion = f"{self.scale}_TO_{target_scale}"
        switcher = {
            'C_TO_F': self.celsius_to_fahrenheit,
            'C_TO_K': self.celsius_to_kelvin,
            'F_TO_C': self.fahrenheit_to_celsius,
            'F_TO_K': self.fahrenheit_to_kelvin,
            'K_TO_C': self.kelvin_to_celsius,
            'K_TO_F': self.kelvin_to_fahrenheit
        }
        func = switcher.get(conversion)
        if func:
            return func()
        else:
            raise ValueError("Invalid temperature conversion.")

    def celsius_to_fahrenheit(self):
        return round((self.measure * 9/5) + 32, 2)

    def celsius_to_kelvin(self):
        return round(self.measure + 273.15, 2)

    def fahrenheit_to_celsius(self):
        return round((self.measure - 32) * 5/9, 2)

    def fahrenheit_to_kelvin(self):
        return round((self.measure + 459.67) * 5/9, 2)

    def kelvin_to_celsius(self):
        return round(self.measure - 273.15, 2)

    def kelvin_to_fahrenheit(self):
        return round(self.measure * 9/5 - 459.67, 2)