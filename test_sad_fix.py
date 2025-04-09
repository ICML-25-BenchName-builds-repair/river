"""Test script to verify the fix for the StandardAbsoluteDeviation class."""

import numpy as np
from river.anomaly import StandardAbsoluteDeviation
from river import stream

def test_sad_functionality():
    # Test with mean
    np.random.seed(42)
    X = np.random.randn(10, 1)
    
    model_mean = StandardAbsoluteDeviation(sub_stat="mean")
    for x, _ in stream.iter_array(X):
        model_mean.learn_one(x)
    
    score_mean = model_mean.score_one({0: 2})
    print(f"Score with mean: {score_mean}")
    
    # Test with median
    model_median = StandardAbsoluteDeviation(sub_stat="median")
    for x, _ in stream.iter_array(X):
        model_median.learn_one(x)
    
    score_median = model_median.score_one({0: 2})
    print(f"Score with median: {score_median}")
    
    return True

if __name__ == "__main__":
    try:
        success = test_sad_functionality()
        print(f"Test {'passed' if success else 'failed'}")
    except Exception as e:
        print(f"Test failed with error: {e}")