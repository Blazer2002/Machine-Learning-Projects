"""
Assignment 2: regression
Goals: introduction to pandas, sklearn, linear and logistic regression, multi-class classification.
Start early, as you will spend time searching for the proper syntax, especially when using pandas
"""

import pandas
from sklearn import linear_model
import matplotlib.pyplot as plt

"""
PART 1: basic linear regression
The goal is to predict the profit of a restaurant, based on the number of habitants where the restaurant 
is located. The chain already has several restaurants in different cities. Your goal is to model 
the relationship between the profit and the populations from the cities where they are located.
Hint: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html 
"""

# Open the csv file RegressionData.csv in Excel, notepad++ or any other applications to have a
# rough overview of the data at hand.
# You will notice that there are several instances (rows), of 2 features (columns).
# The values to be predicted are reported in the 2nd column.

# Load the data from the file RegressionData.csv in a pandas dataframe. Make sure all the instances
# are imported properly. Name the first feature 'X' and the second feature 'y' (these are the labels)
data = pandas.read_csv(filepath_or_buffer = "./RegressionData.csv", header=None, names=['X', 'y'])  # 5 points

# Reshape the data so that it can be processed properly
X = data.values[:,0].reshape(-1, 1) # 5 points
y = data.values[:,1] # 5 points

# Plot the data using a scatter plot to visualize the data
plt.scatter(X, y)  # 5 points
plt.show()

# Linear regression using least squares optimization
reg = linear_model.LinearRegression()  # 5 points
reg.fit(X, y)  # 5 points

# Plot the linear fit
fig = plt.figure()
yPred = reg.predict(X)  # 5 points
plt.scatter(X, y, c='b')  # 5 points
plt.plot(X, yPred, 'r')  # 5 points
fig.canvas.draw()
plt.show()

# # Complete the following print statement (replace the blanks _____ by using a command, do not hard-code the values):
print("The linear relationship between X and y was modeled according to the equation: y = b_0 + X*b_1, \
where the bias parameter b_0 is equal to ", reg.intercept_, " and the weight b_1 is equal to ", reg.coef_[0])
# 8 points

# Predict the profit of a restaurant, if this restaurant is located in a city of 18 habitants
print("the profit/loss in a city with 18 habitants is ", reg.predict([[18]]))
# 8 points

"""
PART 2: logistic regression 
You are a recruiter and your goal is to predict whether an applicant is likely to get hired or rejected. 
You have gathered data over the years that you intend to use as a training set. 
Your task is to use logistic regression to build a model that predicts whether an applicant is likely to
be hired or not, based on the results of a first round of interview (which consisted of two technical questions).
The training instances consist of the two exam scores of each applicant, as well as the hiring decision.
"""

# Open the csv file in Excel, notepad++ or any other applications to have a rough overview of the data at hand.

# Load the data from the file 'LogisticRegressionData.csv' in a pandas dataframe. Make sure all the instances
# are imported properly. Name the first feature 'Score1', the second feature 'Score2', and the class 'y'
data = pandas.read_csv(filepath_or_buffer = "./LogisticRegressionData.csv", header=None, names=['Score1', 'Score2', 'y'])  # 2 points

# Seperate the data features (score1 and Score2) from the class attribute
X = data.values[:,:2]# 2 points
y = data.values[:,2] # 2 points

# Plot the data using a scatter plot to visualize the data.
# Represent the instances with different markers of different colors based on the class labels.
m = ['o', 'x']
c = ['hotpink', '#88c999']
fig = plt.figure()
for i in range(len(data)):
    plt.scatter(data['Score1'][i], data['Score2'][i], marker = m[data['y'][i]],
                color = c[data['y'][i]])  # 2 points
fig.canvas.draw()
plt.show()

# Train a logistic regression classifier to predict the class labels y using the features X
regS = linear_model.LogisticRegression()  # 2 points
regS.fit(X, y)  # 2 points

# Now, we would like to visualize how well does the trained classifier perform on the training data
# Use the trained classifier on the training data to predict the class labels
yPred = regS.predict(X).astype(int)  # 2 points

# To visualize the classification error on the training instances, we will plot again the data. However, this time,
# the markers and colors selected will be determined using the predicted class labels
m = ['o', 'x']
c = ['red', 'blue']  # this time in red and blue
fig = plt.figure()
for i in range(len(data)):
    plt.scatter(data['Score1'][i], data['Score2'][i], marker = m[yPred[i]],
                color = c[yPred[i]])  # 2 points
fig.canvas.draw()
plt.show()
# Notice that some of the training instances are not correctly classified. These are the training errors.

"""
PART 3: Multi-class classification using logistic regression 
Not all classification algorithms can support multi-class classification (classification tasks with more than two classes).
Logistic Regression was designed for binary classification.
One approach to alleviate this shortcoming, is to split the dataset into multiple binary classification datasets 
and fit a binary classification model on each. 
Two different examples of this approach are the One-vs-Rest and One-vs-One strategies.
"""

#  One-vs-Rest method (a.k.a. One-vs-All)

# Explain below how the One-vs-Rest method works for multi-class classification # 12 points
"""
The One-vs-Rest method follows the same binary classification principles; A model is created to classify one output
from the rest. For example, if the output class y contained 3 partitions of outputs, 0, 1, and 2, then a model would be
fitted to classify output 0 from outputs 1 and 2. This model can then predict how likely a data point belongs to
the y=0 partition output.

For as many different output partitions there are, you create the same amount of models for each partition. Each model
will make a prediction and give you the probability of the data point belonging to that partition. The model that
makes a prediction with the greatest probability is the partition that the data point belongs to.
"""

# Explain below how the One-Vs-One method works for multi-class classification # 11 points
"""
The One-vs-One method also follows the same binary classification principles, except this time a model is created to
classify one output from another. For example, if the output class y contained 3 partitions of outputs, 0, 1, and 2,
then 1 model would be fitted to classify output 0 from output 1, while another model would be fitted to classify 
output 0 from output 2. Each of the 2 models can then predict how likely a data point belongs to the y=0 partition 
output.

The number of models to train is determined by this formula: 

Number of models = N * (N-1)/2

In the case of our earlier example, the number of models we need are 3: 0 vs 1, 0 vs 2, and 1 vs 2. Each model will
make a prediction and give you the probability of the data point belonging to that partition. The greatest number of
models that collectively make predictions that it is highly likely that a data point belongs to a partition, will be
the partition that the data point belongs to.

For example: 

if 0 vs 1 predicts a high probability of 1 and
if 0 vs 2 predicts a high probability of 0 and
if 1 vs 2 predicts a high probability of 1, then
since the predictions of a high probability of 1 are greater than the predictions for 0 and 2, 
then the data point maps to y=1.
"""

############## FOR GRADUATE STUDENTS ONLY (the students enrolled in CPS 8318) ##############
""" 
PART 4 FOR GRADUATE STUDENTS ONLY: Multi-class classification using logistic regression project.
Please note that the grade for parts 1, 2, and 3 counts for 70% of your total grade. The following
work requires you to work on a project of your own and will account for the remaining 30% of your grade.

Choose a multi-Class Classification problem with a dataset (with a reasonable size) 
from one of the following sources (other sources are also possible, e.g., Kaggle):

•	UCI Machine Learning Repository, https://archive.ics.uci.edu/ml/datasets.php. 

•	KDD Cup challenges, http://www.kdd.org/kdd-cup.


Download the data, read the description, and use a logistic regression approach to solve a 
classification problem as best as you can. 
Investigate how the One-vs-Rest and One-vs-One methods can help with solving your problem.
Write up a report of approximately 2 pages, double spaced, in which you briefly describe 
the dataset (e.g., the size – number of instances and number of attributes, 
what type of data, source), the problem, the approaches that you tried and the results. 
You can use any appropriate libraries. 


Marking: Part 4 accounts for 30% of your final grade. In the write-up, cite the sources of 
your data and ideas, and use your own words to express your thoughts. 
If you have to use someone else's words or close to them, use quotes and a citation.  
The citation is a number in brackets (like [1]) that refers to a similar number in the references section 
at the end of your paper or in a footnote, where the source is given as an author, title, URL or 
journal/conference/book reference. Grammar is important. 

Submit the python script (.py file(s)) with your redacted document (PDF file) on the D2L site. 
If the dataset is not in the public domain, you also need to submit the data file. 
Name your documents appropriately:
report_Firstname_LastName.pdf
script_ Firstname_LastName.py
"""
