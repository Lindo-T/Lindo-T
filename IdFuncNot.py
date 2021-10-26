#!python3
"""
Identify Function Notation
"""
n_funcs = ["y = x2 + 4x + 1",
    "f(x) = 3x + 7",
    "f(x) = ax2 + bx + c"]
# represent the function in another form
for func in n_funcs:
    f = func.strip()
    if func[0] == "y":
        print(f)
