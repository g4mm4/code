from z3 import *

# define the variables for the serial
s0 = Int('s[0]')
s1 = Int('s[1]')
s2 = Int('s[2]')
s3 = Int('s[3]')
s4 = Int('s[4]')
s5 = Int('s[5]')
s6 = Int('s[6]')
s7 = Int('s[7]')
s8 = Int('s[8]')
s9 = Int('s[9]')
s10 = Int('s[10]')
s11 = Int('s[11]')
s12 = Int('s[12]')
s13 = Int('s[13]')
s14 = Int('s[14]')
s15 = Int('s[15]')
s16 = Int('s[16]')
s17 = Int('s[17]')
s18 = Int('s[18]')
s19 = Int('s[19]')

solver = Solver()

# all serial values are digits between 0 and 9
solver.add(s0 >= 0)
solver.add(s1 >= 0)
solver.add(s2 >= 0)
solver.add(s3 >= 0)
solver.add(s4 >= 0)
solver.add(s5 >= 0)
solver.add(s6 >= 0)
solver.add(s7 >= 0)
solver.add(s8 >= 0)
solver.add(s9 >= 0)
solver.add(s10 >= 0)
solver.add(s11 >= 0)
solver.add(s12 >= 0)
solver.add(s13 >= 0)
solver.add(s14 >= 0)
solver.add(s15 >= 0)
solver.add(s16 >= 0)
solver.add(s17 >= 0)
solver.add(s18 >= 0)
solver.add(s19 >= 0)
solver.add(s0 < 10)
solver.add(s1 < 10)
solver.add(s2 < 10)
solver.add(s3 < 10)
solver.add(s4 < 10)
solver.add(s5 < 10)
solver.add(s6 < 10)
solver.add(s7 < 10)
solver.add(s8 < 10)
solver.add(s9 < 10)
solver.add(s10 < 10)
solver.add(s11 < 10)
solver.add(s12 < 10)
solver.add(s13 < 10)
solver.add(s14 < 10)
solver.add(s15 < 10)
solver.add(s16 < 10)
solver.add(s17 < 10)
solver.add(s18 < 10)
solver.add(s19 < 10)

# add serial checking conditions
solver.add(s15 + s4 == 10)
solver.add(s1 * s18 == 2 )
solver.add(s15 / s9 == 1)
solver.add(s17 - s0 == 4)
solver.add(s5 - s17 == -1)
solver.add(s15 - s1 == 5)
solver.add(s1 * s10 == 18)
solver.add(s8 + s13 == 14)
solver.add(s18 * s8 == 5)
solver.add(s4 * s11 == 0)
solver.add(s8 + s9 == 12)
solver.add(s12 - s19 == 1)
solver.add(s9 % s17 == 7)
solver.add(s14 * s16 == 40)
solver.add(s7 - s4 == 1)
solver.add(s6 + s0 == 6)
solver.add(s2 - s16 == 0)
solver.add(s4 - s6 == 1)
solver.add(s0 % s5 == 4)
solver.add(s5 * s11 == 0)
solver.add(s10 % s15 == 2)
solver.add(s11 / s3 == 0)
solver.add(s14 - s13 == -4)
solver.add(s18 + s19 == 3)

# s3 can't be 0 because of division by zero
solver.add(s3 != 0)

print("solving...")
print(solver.check())
print(solver.model())