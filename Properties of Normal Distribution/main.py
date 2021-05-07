import csv
import pandas as pd
import statistics as st
import plotly.figure_factory as ff

# Opening the file using the open function and stoaring it in a variable
File_Object = pd.read_csv('archive (1)\StudentsPerformance.csv')

# Creating a list stoaring all the scores of reading marks in a var
Reading_Marks = File_Object["writing score"].tolist()

#mean,median,mode and standardDeviation
mean = st.mean(Reading_Marks)
median = st.median(Reading_Marks)
mode = st.mode(Reading_Marks)

sd = st.stdev(Reading_Marks)

# Printing the mean median mode and std
print("mean -> " + str(mean))
print("median -> " + str(median))
print("mode -> " + str(mode))
print("Std -> " + str(sd))

# Finding the first_std,second_std,third_std
first_std_start, first_std_end = mean - sd, mean + sd
second_std_start, second_std_end = mean - (2*sd), mean + (2*sd)
third_std_start, third_std_end = mean - (3*sd), mean + (3*sd)

thin_1_std = [result for result in Reading_Marks if result >
              first_std_start and result < first_std_end]
thin_2_std = [result for result in Reading_Marks if result >
              second_std_start and result < second_std_end]
thin_3_std = [result for result in Reading_Marks if result >
              third_std_start and result < third_std_end]

print('thin_1_std: ' + str(thin_1_std))
print('thin_2_std: ' + str(thin_2_std))
print('thin_3_std: ' + str(thin_3_std))

#fig = ff.create_distplot([Reading_Marks], ['marks'], show_hist=False)
# fig.show()