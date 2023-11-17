import unittest 
from datetime import datetime 

def valid_input(symbol, chart_type, time_series, start_date, end_date):
    if not(symbol.isalpha() and symbol.isupper() and 1 <= len(symbol) <= 7):
        return False
    if not(chart_type.isdigit() and chart_type in ['1', '2']):
        return False
    if not(time_series.isdigit() and 1 <=int(time_series) <= 4):
        return False  
    try:
        datetime.strptime(start_date, "%Y-%m-%d")
        datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        return False

    return True

class TestUserInputs(unittest.TestCase):
    def test_valid_inputs(self):
        self.assertTrue(valid_input("IBM", "1", "1", "2020-01-01", "2021-01-01"))
    
    def test_symbol_validation(self):
        self.assertFalse(valid_input("321", "1", "2", "2020-01-01", "2021-01-01"))

    def test_chartType_validation(self):
        self.assertFalse(valid_input("IBM", "3", "2", "2020-01-01", "2021-01-01"))
    
    def test_timeSeries_validation(self):
        self.assertFalse(valid_input("IBM", "1", "5", "2020-01-01", "2021-01-01"))

    def test_dateTimeStart_validation(self):
        self.assertFalse(valid_input("IBM", "1", "2", "07-17-2000", "2021-01-01"))

    def test_dateTimeEnd_validation(self):
        self.assertFalse(valid_input("321", "1", "2", "2020-01-01", "07-17-2000"))

if __name__ == "__main__":
    unittest.main()