"""Test script to reproduce the mypy issue in the StandardAbsoluteDeviation class."""

from river import anomaly, stats

# This is just to demonstrate the type issue
def test_sad_type_issue():
    # Initialize with "mean"
    sad_mean = anomaly.StandardAbsoluteDeviation(sub_stat="mean")
    print(f"Type of subtracted_statistic_estimator with mean: {type(sad_mean.subtracted_statistic_estimator)}")
    
    # Initialize with "median"
    sad_median = anomaly.StandardAbsoluteDeviation(sub_stat="median")
    print(f"Type of subtracted_statistic_estimator with median: {type(sad_median.subtracted_statistic_estimator)}")
    
    # The issue is that mypy sees these as different types, even though they share the same interface

if __name__ == "__main__":
    test_sad_type_issue()