class Calculator:
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        result = a + b
        self._log(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        result = a - b
        self._log(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        result = a * b
        self._log(f"{a} × {b} = {result}")
        return result
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self._log(f"{a} ÷ {b} = {result}")
        return result
    
    def power(self, a, b):
        result = a ** b
        self._log(f"{a} ^ {b} = {result}")
        return result
    
    def sqrt(self, a):
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number")
        result = a ** 0.5
        self._log(f"√{a} = {result}")
        return result
    
    def _log(self, operation):
        self.history.append(operation)
    
    def get_history(self):
        return self.history
    
    def clear_history(self):
        self.history = []


def main():
    calc = Calculator()
    
    print("=" * 40)
    print("   🧮 PYTHON CALCULATOR 🧮")
    print("=" * 40)
    
    # Demo operations
    print("\n📊 Demo Calculations:")
    print(f"10 + 5 = {calc.add(10, 5)}")
    print(f"20 - 8 = {calc.subtract(20, 8)}")
    print(f"7 × 6 = {calc.multiply(7, 6)}")
    print(f"100 ÷ 4 = {calc.divide(100, 4)}")
    print(f"2 ^ 10 = {calc.power(2, 10)}")
    print(f"√144 = {calc.sqrt(144)}")
    
    print("\n📜 Calculation History:")
    for i, entry in enumerate(calc.get_history(), 1):
        print(f"  {i}. {entry}")
    
    # Interactive mode
    print("\n" + "=" * 40)
    print("   INTERACTIVE MODE")
    print("   Commands: +, -, *, /, ^, sqrt, history, quit")
    print("=" * 40)
    
    while True:
        try:
            command = input("\nEnter operation (+, -, *, /, ^, sqrt) or 'quit': ").strip().lower()
            
            if command == 'quit':
                print("👋 Goodbye!")
                break
            elif command == 'history':
                for i, entry in enumerate(calc.get_history(), 1):
                    print(f"  {i}. {entry}")
                continue
            
            if command == 'sqrt':
                num = float(input("Enter number: "))
                result = calc.sqrt(num)
                print(f"Result: {result}")
            else:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if command == '+':
                    result = calc.add(num1, num2)
                elif command == '-':
                    result = calc.subtract(num1, num2)
                elif command == '*':
                    result = calc.multiply(num1, num2)
                elif command == '/':
                    result = calc.divide(num1, num2)
                elif command == '^':
                    result = calc.power(num1, num2)
                else:
                    print("❌ Unknown operation")
                    continue
                
                print(f"Result: {result}")
                
        except ValueError as e:
            print(f"❌ Error: {e}")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")


if __name__ == "__main__":
    main()
