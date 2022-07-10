# Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import codecademylib3

# Read in the data
codecademy = pd.read_csv('codecademy.csv')

# Print the first five rows
#print(codecademy.head())

# Create a scatter plot of score vs completed
#plt.scatter(x=codecademy['completed'], y=codecademy['score'])
#plt.show()
#plt.clf()

# Fit a linear regression to predict score based on prior lessons completed
model = sm.OLS.from_formula('score ~ completed', data = codecademy)
results = model.fit()
#print(results.params) #Intercept: 13.214113, completed: 1.306826
#score = 1.3*completed + 13.21
intercept = results.params[0]
slope = results.params[1]
#print(slope)
#print(intercept)

# Intercept interpretation:
#The expected score for someone who did not complete any other content items prior to the quiz is 13.21 points

# Slope interpretation:
#There is an average 1.3 point increase in score for each additional item completed prior to the quiz 

# Plot the scatter plot with the line on top
plt.scatter(x=codecademy['completed'], y=codecademy['score'])
plt.xlabel('# of other content items completed prior to quiz')
plt.ylabel('Quiz score')
plt.plot(codecademy['completed'], results.predict(codecademy))
plt.show()
plt.clf()

# Predict score for learner who has completed 20 prior lessons
#print(20*slope + intercept)

# Calculate fitted values
fitted_values = results.predict(codecademy)

# Calculate residuals
residuals = codecademy['score'] - fitted_values

# Check normality assumption
plt.hist(residuals)
plt.show()
plt.clf()

# Check homoscedasticity assumption
plt.scatter(x=fitted_values, y=residuals)
plt.show()
plt.clf()

# Create a boxplot of score vs lesson
sns.boxplot(x='lesson', y='score', data=codecademy)
plt.show()
plt.clf()

# Fit a linear regression to predict score based on which lesson they took
lesson_model = sm.OLS.from_formula('score ~ lesson', data = codecademy)
lesson_results = lesson_model.fit()
print(lesson_results.params)
#Intercept = 59.220
#lesson[T.LessonB] = -11.642
lesson_intercept = lesson_results.params[0]
lesson_slopeTB = lesson_results.params[1]

# Calculate and print the group means and mean difference (for comparison)
mean_lesson_A = np.mean(codecademy['score'][(codecademy['lesson'] == 'Lesson A')])
print('Mean Score for Lesson A: ', mean_lesson_A) #59.22

mean_lesson_B = np.mean(codecademy['score'][(codecademy['lesson'] == 'Lesson B')])
print('Mean Score for Lesson B: ', mean_lesson_B) #47.58

# Use `sns.lmplot()` to plot `score` vs. `completed` colored by `lesson`
sns.lmplot(x = 'completed', y = 'score', hue = 'lesson', data = codecademy)
plt.show()
plt.clf()