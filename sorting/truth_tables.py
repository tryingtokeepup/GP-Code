

for A in [False, True]:
    for B in [False, True]:
        for C in [False, True]:
            print(f"{A} -- {B} -- {C} --- {(A or B)}")
