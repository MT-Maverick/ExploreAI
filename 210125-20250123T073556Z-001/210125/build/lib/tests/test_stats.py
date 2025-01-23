from weather_analysis.stats import column_stats
import pandas as pd

def test_column_stats():
    sample_data = pd.DataFrame({'min_temp': [10,11,12,9,8]})
    stats = column_stats(sample_data, 'min_temp')
    assert stats['mean'] == 10
    assert stats['median'] == 10
    assert stats['std_dev'] > 0