"""Simple Python loop examples."""


def for_loop_example():
    print("=== for loop ===")
    for i in range(1, 6):
        print(f"Count: {i}")


def while_loop_example():
    print("=== while loop ===")
    n = 1
    while n <= 5:
        print(f"Number: {n}")
        n += 1


def nested_loop_example():
    print("=== nested loop (multiplication table 1-3) ===")
    for i in range(1, 4):
        for j in range(1, 4):
            print(f"{i} x {j} = {i * j}")
        print("---")


def list_loop_example():
    print("=== loop over a list ===")
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(f"Fruit: {fruit}")


if __name__ == "__main__":
    for_loop_example()
    print()
    while_loop_example()
    print()
    nested_loop_example()
    print()
    list_loop_example()
