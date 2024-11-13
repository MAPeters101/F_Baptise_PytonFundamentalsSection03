"""
Exercise 1
Given two floats a and b, and some tolerance tol,
write an expression that will test whether a and b are within tol of each other.
"""
a = 1.01
b = 1.009
tol = 0.0011
print(a - b)
print(abs(a - b) <= tol)
print('='*80)


"""
Exercise 2
Assume you have some variable elapsed that contains elapsed time in seconds.

Create three new variables: hours, minutes and seconds, that represent the 
number of hours, minutes and seconds represented by elapsed.

For example, if elapsed = 7835, then hours = 2, minutes = 10 and seconds = 35

"""

elapsed = 7835
hours = elapsed // (60 * 60)
minutes = (elapsed - hours*60*60) // 60
seconds = elapsed - hours*60*60 - minutes*60
print(f'{elapsed:=} = {hours:=}, {minutes:=}, {seconds:=}')



