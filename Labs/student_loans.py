#Jeanna Shellenberger Section 061
print('Welcome to the Student Loan Calculator')
print('Enter the amount of the loan in dollars with (no commas):')

P = float(input(''))  #amount of money loaned

print('Enter the number of years the loan will be for:')

y = int(input(''))  #years
t = 12 #times compounded monthly
i1 = 0.034 #rate of subsidized loan
i2 = 0.068 #rate of unsubsidized loan
i3 = 0.079 #rate of federal plus loan
f1 = 0.01051 #fee rate of subsidized and unsubsidized
f2 = 0.04204 #fee rate of federal plus

#Subsidized Loans
M1 = (P * i1) / (t * (1 - pow(1 + (i1 / t) ,(-y * t)))) #monthly payment
B1 = M1 * t * y #balance
I1 = B1 - P #interest paid
F1 = P * f1 #fees

#Unsubsidized Loans
P2 = P * (1 + i2 * 4.25) #new amount loaned
M2 = (P2 * i2) / (t * (1 - pow(1 + (i2 / t),(-y * t)))) #monthly payment
B2 = M2 * t * y #balance
I2 = B2 - P #interest paid
F2 = P * f1 #fees

#Federal Plus Loans
P3 = P * (1 + (i3 * 4.25)) #new amount loaned
M3 = (P3 * i3) / (t * (1 - pow(1 + (i3 / t),(-y * t)))) #monthly payment
B3 = M3 * t * y #balance
I3 = B3 - P #interest paid
F3 = P * f2 #fees

print('\nSubsidized Federal Direct Loan')
print('Principle:', int(P))
print('Interest Rate:', round(float((i1 * 100)),2))
print('Years:', int(y))
print('Monthly Payment', round(M1,2))
print('Total Paid on Loan:', round(B1,2))
print('Total Interest Paid:', round(I1,2))
print('Additional Fees Paid:', round(F1,2))
print('Total Costs Over Principle:', round(I1 + F1,2))

print('\nUnsubsidized Federal Direct Loan')
print('Principle:', int(P))
print('Interest Rate:', round(float((i2 * 100)),2))
print('Years:', int(y))
print('Monthly Payment', round(M2,2))
print('Total Paid on Loan', round(B2,2))
print('Total Interest Paid:', round(I2,2))
print('Additional Fees Paid:', round(F2,2))
print('Total Costs Over Principle:', round(I2 + F2,2))

print('\nFederal Plus Loan')
print('Principle:', int(P))
print('Interest Rate:', round(float((i3 * 100)),2))
print('Years:', int(y))
print('Monthly Payment', round(M3,2))
print('Total Paid on Loan:', round(B3,2))
print('Total Interest Paid:', round(I3,2))
print('Additional Fees Paid:', round(F3,2))
print('Total Costs Over Principle:', round(I3 + F3,2))
