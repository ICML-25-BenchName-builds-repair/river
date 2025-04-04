"""Test script to verify the mypy issue in the SAD class."""

from river import stats
from river.anomaly.sad import StandardAbsoluteDeviation

# Create a SAD instance with mean
sad_mean = StandardAbsoluteDeviation(sub_stat="mean")
print(f"Mean SAD: {type(sad_mean.subtracted_statistic_estimator)}")

# Create a SAD instance with median
sad_median = StandardAbsoluteDeviation(sub_stat="median")
print(f"Median SAD: {type(sad_median.subtracted_statistic_estimator)}")

# Test functionality
sad_mean.learn_one({0: 1.0})
sad_median.learn_one({0: 1.0})

print(f"Mean SAD score: {sad_mean.score_one({0: 2.0})}")
print(f"Median SAD score: {sad_median.score_one({0: 2.0})}")