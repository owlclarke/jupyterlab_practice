# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.6
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Graeme Clarke
# Notebook for Assignment 7.

# %%
def compute_mean(values):
    if not values:
        return 0  # Return 0 if the list is empty to avoid division by zero
    mean_value = sum(values) / len(values)
    print(mean_value)

# Call the function with the specified list
compute_mean([2, 4, 6, 8])

# %% [markdown]
# ### Explanation of Code
#
# The code above defines a function called `compute_mean` that takes a list of values as input and calculates the mean (average) of those values. The function sums all the values in the list and then divides the sum by the number of values in the list. It prints the resulting mean.
#
# #### Equation of the Mean
#
# The mean of a list of values \( x_1, x_2, \ldots, x_n \) can be expressed as:
#
# $$ \text{Mean} = \frac{1}{n} \sum_{i=1}^{n} x_i $$
#
# Alternatively, it can also be written as:
#
# $$ \mu = \frac{\sum_{i=1}^{n} x_i}{n} $$
#
# Where:
# - \( \mu \) represents the mean
# - \( x_i \) are the values in the list
# - \( n \) is the number of values in the list

# %% [markdown]
# ### Citation 
# For the third cell above (Explanation of Code) I used help from Microsoft Copilot along with the reference documents in the assignment. I do not claim originality or ownership for the code, and am using it for demonstrative purposes only. 

# %%
