from weather_analysis.loader import load_data

def test_load_data():
    file_path =  'C:\\Users\\HP\\Downloads\\trial\\chart.csv'
    data = load_data(file_path)
    assert not data.empty, "Data should not be empty"
