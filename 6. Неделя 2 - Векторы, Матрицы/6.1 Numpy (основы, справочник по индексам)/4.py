a_с = A2 - A1
b_с = A3 - A2
c_с = A1 - A3
a = (a_с[0] ** 2 + a_с[1] ** 2) ** 0.5
b = (b_с[0] ** 2 + b_с[1] ** 2) ** 0.5
c = (c_с[0] ** 2 + c_с[1] ** 2) ** 0.5
p = (a + b + c) / 2
S = (p * (p - a) * (p - b) * (p - c)) ** 0.5

print(S)
