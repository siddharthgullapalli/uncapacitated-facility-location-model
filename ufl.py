from __future__ import print_function
import sys
import cplex
from cplex.exceptions import CplexError

n = 6
m = 5
r = 36
my_colnames = []
my_rownames = []

for i in range(n):
    for j in range(m):
     my_colnames.append('X'+str(i+1)+','+str(j+1))

for j in range(m):
 my_colnames.append('Y'+str(i+1)+','+str(j+1))
for j in range(r):
    my_rownames.append('r'+str(j+1))


my_obj = [12,13,6,0,1,8,4,9,1,2,2,6,6,0,1,3,5,2,1,8,8,0,5,10,8,2,0,3,4,1,4,3,4,4,7]
my_rhs = []
for i in range(n):
    my_rhs.append(int(1))
for j in range(n * m):
    my_rhs.append(int(0))
my_lb = []
my_ub = []
for i in range(r-1):
    my_lb.append(int(0.0))
for i in range(r-1):
    my_ub.append(int(1.0))

my_sense ="E"*6 + "L"*30
my_ctype ="B"*35


try:
    my_prob = cplex.Cplex()

    my_prob.objective.set_sense(my_prob.objective.sense.minimize)

    my_prob.variables.add(obj=my_obj, lb=my_lb, ub=my_ub, types=my_ctype, names=my_colnames)
    d2 = []
    d3 = [1 for i in range(m * n)]
    d4 = []
    for i in range(6):
        d2.append([my_colnames[i * 5:(i + 1) * 5], d3[i * 5:(i + 1) * 5]])


    d4.extend(my_colnames[30:])
    d6 = []
    d7 = []
    for i in range(m * n):
        d6.append([int(1), int(-1)])

    for i in range(5):
        for j in range(6):
            d7.append([[my_colnames[i + j * 5], d4[i]], [1, -1]])
    rows = d2+d7



    my_prob.linear_constraints.add(lin_expr=rows, senses=my_sense,rhs=my_rhs, names=my_rownames)

    my_prob.solve()

except CplexError as exc:
    print(exc)
    sys.exit()

print("hello")

print()

print("Solution status = ", my_prob.solution.get_status(), ":", end=' ')

print(my_prob.solution.status[my_prob.solution.get_status()])


print("Solution value  = ", my_prob.solution.get_objective_value())

x = my_prob.solution.get_values()
print(x)


sys.exit()




