import scipy.stats as stats

# Example data: Assume these are past observations
# Total number of days observed
total_days = 10
# Number of days it rained
rainy_days = 7

# Calculate the proportion of rainy days
p_hat = rainy_days / total_days

# Confidence level
confidence_level = 0.90
alpha = 1 - confidence_level

# Calculate the z-score for the 90% confidence level
z_score = stats.norm.ppf(1 - alpha / 2)

# Standard error for proportion
standard_error = (p_hat * (1 - p_hat) / total_days) ** 0.5

# Confidence interval
margin_of_error = z_score * standard_error
confidence_interval = (p_hat - margin_of_error, p_hat + margin_of_error)

print("Estimated Probability of Rain:", p_hat)
print("90% Confidence Interval:", confidence_interval)
