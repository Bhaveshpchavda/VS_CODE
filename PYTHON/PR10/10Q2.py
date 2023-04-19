import matplotlib.pyplot as plt

# frequency distribution table for theory marks 
theory_marks = [0, 20, 40, 60, 80, 100] 
theory_students = [6, 22, 46, 18, 8, 0] 

# frequency distribution table for practical marks
practical_marks = [0, 20, 40, 60, 80, 100] 
practical_students = [10, 28, 12, 18, 32, 0] 

# create figure object
fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True)

# plot histograms
ax1.hist(theory_marks, bins=theory_marks, weights=theory_students, color='green') 
ax1.set_xlabel('Marks') 
ax1.set_ylabel('Number of Students') 
ax1.set_title('Histogram of Theory Examination Results') 

ax2.hist(practical_marks, bins=practical_marks, weights=practical_students, color='red') 
ax2.set_xlabel('Marks') 
ax2.set_title('Histogram of Practical Examination Results') 

# show figure
plt.show()
