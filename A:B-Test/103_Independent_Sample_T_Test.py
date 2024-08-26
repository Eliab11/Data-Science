####################################################################################
# One sample T-Test
####################################################################################



# IMPORT REQUIRED PACKAGES 

import numpy as  np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind, norm


#  CREATE MOCK DATA


Sample_A = norm.rvs(loc = 500, scale = 100, size = 250, random_state = 42).astype(int)
Sample_B = norm.rvs(loc = 550, scale = 150, size = 100, random_state = 42).astype(int)



plt.hist(Sample_A, density = True, alpha = 0.5)
plt.hist(Sample_B, density = True, alpha = 0.5)
plt.show()


Sample_A_mean = Sample_A.mean()
Sample_B_mean = Sample_B.mean()
print(Sample_A_mean, Sample_B_mean)


# SET THE HYPOTHESES & ACCEPTANCE CRITERIA


null_hypothesis = "The mean of the sample is equal to the mean of the population"
alternate_hypothesis = "The mean of the sample is different to the mean of the population"
acceptance_criteria = 0.05

#    EXECUTE THE HYPOTHESIS TEST

t_statistic, p_value = ttest_ind(Sample_A, Sample_B)
print(t_statistic, p_value)

if p_value <= acceptance_criteria:
    print(f"As our p-value of  {p_value} is lower than our acceptance_criteria  of {acceptance_criteria} - we reject the null hypothesis, and conclude that: {alternate_hypothesis}" )
else:
    print(f"As our cp-value of  {p_value} is higher than our acceptance_criteria of {acceptance_criteria} - we reject the null hypothesis, and conclude that: {alternate_hypothesis}" )  
    
    
# WELCH'S T-TEST 



# EXECUTE THE HYPOTHESIS TEST
t_statistic, p_value = ttest_ind(Sample_A, Sample_B, equal_var = False)
print(t_statistic, p_value)

# PRINT THE RESULT (p-value)

if p_value <= acceptance_criteria:
    print(f"As our p-value of  {p_value} is lower than our acceptance_criteria  of {acceptance_criteria} - we reject the null hypothesis, and conclude that: {alternate_hypothesis}" )
else:
    print(f"As our cp-value of  {p_value} is higher than our acceptance_criteria of {acceptance_criteria} - we reject the null hypothesis, and conclude that: {alternate_hypothesis}" )  
    
    
   