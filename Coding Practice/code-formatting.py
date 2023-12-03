class InvalidName:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"Name: {self.name}")


def calculate_sum(a, b):
    return a + b


def main():
    num1 = 10
    num2 = 5
    sum_result = calculate_sum(num1, num2)
    print(f"The sum is: {sum_result}")


if __name__ == "__main__":
    main()
