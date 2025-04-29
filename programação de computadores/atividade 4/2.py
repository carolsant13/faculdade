print("Tabuada de 1 a 10:")
print("-" * 30)

for i in range(1, 11):

    for j in range(1, 11):
        print(f"{i} × {j} = {i*j}", end="\t")
    print()
