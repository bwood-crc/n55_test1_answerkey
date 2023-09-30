from SavingsAccount import *

s1 = SavingsAccount("Our Savings")
s2 = SavingsAccount("Kids Savings")

# The following shouldn't be possible since it's abstract.
# a1 = Account("Generic Account 1")

s1.deposit(Decimal(10.00))
s1.withdraw(Decimal(5.00))

print(s1)
print(s2)
