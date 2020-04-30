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
# my version of Megumin
# print(round(int(data['Pclass'].value_counts()[1])/int(data.shape[0])*100, 2))
task3 = open('answers/task_3.txt', 'w')
task3.write(str(round(int(data.loc[data['Pclass'] == 1].count()[1])/int(data.shape[0])*100, 2)))
task3.close()

# Task 4
# my version of MAximus
with open('answers/task_4.txt', 'w') as task4:
    mean_age = round(data['Age'].mean(axis=0), 2)
    task4.write(str(mean_age))
    median_age = round(data['Age'].median(axis=0), 2)
    task4.write(' ' + str(median_age))

# Task 5
# my version of Konosuba
# print(round(data.corr(method='pearson')['Parch'].loc['SibSp'], 2))
with open('answers/task_5.txt', 'w') as task5:
    task5.write(str(round(data.corr(method='pearson')['Parch'].loc['SibSp'], 2)))

# Task 6
# my version
female_memes = data.loc[data['Sex'] == 'female']['Name']
female_mode_name = pd.Series(['0'], index=[0])
index = 0
'''
for i in female_memes:
    
    if i.split(' ')[1]:
        female_mode_name = female_mode_name.append(pd.Series(i.split(' ')[2], index=[index]))
    else:
        fdsfdsfsf
print(female_mode_name)
print(female_mode_name.mode())

'''
for i in female_memes:
    index += 1
    without_surname = i.split(',')
    if without_surname[1].split(' ')[1] == 'Mrs.' or without_surname[1].split(' ')[1] == 'the':
        print(without_surname[1].split('('))
    else:
        female_mode_name = female_mode_name.append(pd.Series(without_surname[1].split(' ')[2], index=[index]))
index = 0
print(female_mode_name)
# Test
# data_v1 = data.loc[data['Sex'] == 'female']

