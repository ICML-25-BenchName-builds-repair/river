from river import anomaly

# Test with mean
model_mean = anomaly.StandardAbsoluteDeviation(sub_stat="mean")
model_mean.learn_one({0: 1.0})
score_mean = model_mean.score_one({0: 2.0})
print(f"Score with mean: {score_mean}")

# Test with median
model_median = anomaly.StandardAbsoluteDeviation(sub_stat="median")
model_median.learn_one({0: 1.0})
score_median = model_median.score_one({0: 2.0})
print(f"Score with median: {score_median}")