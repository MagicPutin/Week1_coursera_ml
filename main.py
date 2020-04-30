import numpy as np
import pandas as pd

data = pd.read_csv('data/titanic.csv', index_col='PassengerId')
# Task 1
# my version
# print(data.loc[data['Sex'] == 'female'])
# print(data.loc[data['Sex'] == 'male'])

# cool version
task1 = open('answers/task_1.txt', 'w')
task1.write(str(data['Sex'].value_counts()[0]) + ' ' + str(data['Sex'].value_counts()[1]))
task1.close()
# print(data['Sex'].value_counts())

# Task 2
# my version is the coolest
# print(round(int(data['Survived'].value_counts()[1])/int(data.shape[0])*100, 2))
task2 = open('answers/task_2.txt', 'w')
task2.write(str(round(int(data['Survived'].value_counts()[1])/int(data.shape[0])*100, 2)))
task2.close()

# Task 3
# my version is Megumin
# print(round(int(data['Pclass'].value_counts()[1])/int(data.shape[0])*100, 2))
task3 = open('answers/task_3.txt', 'w')
task3.write(str(round(int(data.loc[data['Pclass'] == 1].count()[1])/int(data.shape[0])*100, 2)))
task3.close()

# Task 4

# Test
# data_v1 = data.loc[data['Sex'] == 'female']
# print('')
