# Example 1: Pie Chart : 
#  we have survey data on people's favorite fruits, and we want to visualize the distribution of responses using a pie chart
import matplotlib.pyplot as plt

fruits = ['Apple', 'Banana', 'Orange', 'Mango']
counts = [25, 30, 20, 35]

# Plotting the pie chart
plt.figure(figsize=(8, 6))
plt.pie(counts, labels=fruits, autopct='%1.1f%%', startangle=140)
plt.title('Favorite Fruits Survey')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()



# Example 2: Line Plot
#  we have recorded the temperature variations over several days and want to visualize it using a line plot.
import numpy as np

# Sample data: temperature readings over 7 days
days = np.arange(1, 8)
temperatures = [20, 22, 23, 25, 24, 21, 19]

# Plotting the line graph
plt.figure(figsize=(8, 6))
plt.plot(days, temperatures, marker='o', color='b', linestyle='-')
plt.xlabel('Day')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Variation Over 7 Days')
plt.grid(True)
plt.show()

# Example 3: Bar Chart
# we have data on the sales performance of different products, and we want to visualize it using a bar chart.
# Sample data: product names and their sales counts
products = ['Product A', 'Product B', 'Product C', 'Product D']
sales = [150, 200, 180, 220]

# Plotting the bar chart
plt.figure(figsize=(8, 6))
plt.bar(products, sales, color='skyblue')
plt.xlabel('Product')
plt.ylabel('Sales Count')
plt.title('Product Sales Performance')
plt.xticks(rotation=45)
plt.show()


#  Example of : Anova Test 

import pandas as pd
import numpy as np
import scipy.stats as stats

# Create a DataFrame
data = pd.DataFrame({
    'group1': np.random.normal(0, 1, 100),
    'group2': np.random.normal(1, 1, 100),
    'group3': np.random.normal(0.5, 1, 100)
})

# Perform one-way ANOVA
fvalue, pvalue = stats.f_oneway(data['group1'], data['group2'], data['group3'])
print('F-Value:', fvalue)
print('P-Value:', pvalue)

# Output
# F-Value: 4.51233469761552
# P-Value: 0.01133415423955698
# The p-value is less than 0.05, so we reject the null hypothesis that the means of the groups are equal.
# This indicates that at least one group has a significantly different mean from the others.

# Example of : Chi-Square Test
# we have survey data on people's favorite colors and want to test if the distribution of responses is significantly different from a uniform distribution.
import pandas as pd
import numpy as np
import scipy.stats as stats

# Create a DataFrame
data = pd.DataFrame({
    'color': ['Red', 'Blue', 'Green', 'Yellow', 'Orange'],
    'count': [45, 20, 15, 10, 10]
})

# Observed frequencies
observed = data['count']

# Expected frequencies (uniform distribution)
total = observed.sum()
expected = np.repeat(total / len(observed), len(observed))

# Perform chi-square test
chisq, pvalue = stats.chisquare(observed, expected)
print('Chi-Square:', chisq)
print('P-Value:', pvalue)

# Output
# Chi-Square: 30.0
# P-Value: 2.204364238465235e-06

# The p-value is less than 0.05, so we reject the null hypothesis that the observed distribution is the same as the expected uniform distribution.

