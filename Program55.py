"""
Exception Handling	Write a program for converting weight from Pound to Kilo grams.
a) Use assertion for the negative weight.
b) Use assertion to weight more than 100 KG
"""

"""Function to convert pounds to kg and to check that the weight should not be negative"""
def poundsTokgs(pound):
    print("\na)Converting non negative weight as pounds to kgs")
    try:
        assert(pound>=0),"Cannot accept negative weight"
        return("The weight in kg is: ",pound*0.453592)
    except AssertionError as AErr:
        return("Your weight is of negative value.")
        return("Error is ",AErr)

"""Function to convert pounds to kg and to check that the weight should be greater than 100kgs"""
def weight100plus(pound):
    print("\nb)Converting weight as pounds to kgs greater than 100kgs")
    try:
        weightInkg = pound*0.453592
        assert(weightInkg>=100),"Cannot accept weight lesser than 100kgs"
        return("The weight in kg is: ",weightInkg)
    except AssertionError as AErr:
        return("Your weight is less than 100kgs, please try again.")
        return("Error is ",AErr)

print("\n",poundsTokgs(6))
print("\n",poundsTokgs(-45))


print("\n",weight100plus(5))
print("\n",weight100plus(400))


# Output:

# C:\Users\faraz\Desktop\Python\Pes_Python_Assignments-3>python Program55.py

# a)Converting non negative weight as pounds to kgs

#  ('The weight in kg is: ', 2.721552)

# a)Converting non negative weight as pounds to kgs       

#  Your weight is of negative value.

# b)Converting weight as pounds to kgs greater than 100kgs

#  Your weight is less than 100kgs, please try again.

# b)Converting weight as pounds to kgs greater than 100kgs

#  ('The weight in kg is: ', 181.4368)

# C:\Users\faraz\Desktop\Python\Pes_Python_Assignments-3>