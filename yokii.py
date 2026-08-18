import math
import re

class Calculator:
    """A comprehensive calculator with all possible operations"""
    
    def __init__(self):
        self.history = []
    
    # Basic Operations
    def add(self, a, b):
        """Addition"""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """Subtraction"""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """Multiplication"""
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a, b):
        """Division"""
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def floor_divide(self, a, b):
        """Floor Division"""
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        result = a // b
        self.history.append(f"{a} // {b} = {result}")
        return result
    
    def modulo(self, a, b):
        """Modulo (Remainder)"""
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        result = a % b
        self.history.append(f"{a} % {b} = {result}")
        return result
    
    # Power Operations
    def power(self, base, exponent):
        """Power/Exponentiation"""
        result = base ** exponent
        self.history.append(f"{base} ** {exponent} = {result}")
        return result
    
    def square(self, a):
        """Square (x^2)"""
        result = a ** 2
        self.history.append(f"{a}^2 = {result}")
        return result
    
    def cube(self, a):
        """Cube (x^3)"""
        result = a ** 3
        self.history.append(f"{a}^3 = {result}")
        return result
    
    # Root Operations
    def square_root(self, a):
        """Square Root"""
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number!")
        result = math.sqrt(a)
        self.history.append(f"√{a} = {result}")
        return result
    
    def cube_root(self, a):
        """Cube Root"""
        result = a ** (1/3) if a >= 0 else -((-a) ** (1/3))
        self.history.append(f"∛{a} = {result}")
        return result
    
    def nth_root(self, a, n):
        """Nth Root"""
        if n == 0:
            raise ValueError("Root cannot be 0!")
        if a < 0 and n % 2 == 0:
            raise ValueError("Cannot calculate even root of negative number!")
        result = a ** (1/n) if a >= 0 else -((-a) ** (1/n))
        self.history.append(f"Root({a}, {n}) = {result}")
        return result
    
    # Trigonometric Functions
    def sine(self, angle_deg):
        """Sine (input in degrees)"""
        angle_rad = math.radians(angle_deg)
        result = math.sin(angle_rad)
        self.history.append(f"sin({angle_deg}°) = {result}")
        return result
    
    def cosine(self, angle_deg):
        """Cosine (input in degrees)"""
        angle_rad = math.radians(angle_deg)
        result = math.cos(angle_rad)
        self.history.append(f"cos({angle_deg}°) = {result}")
        return result
    
    def tangent(self, angle_deg):
        """Tangent (input in degrees)"""
        angle_rad = math.radians(angle_deg)
        result = math.tan(angle_rad)
        self.history.append(f"tan({angle_deg}°) = {result}")
        return result
    
    def arcsine(self, value):
        """Arc Sine (inverse sin)"""
        if value < -1 or value > 1:
            raise ValueError("Value must be between -1 and 1!")
        result = math.degrees(math.asin(value))
        self.history.append(f"arcsin({value}) = {result}°")
        return result
    
    def arccosine(self, value):
        """Arc Cosine (inverse cos)"""
        if value < -1 or value > 1:
            raise ValueError("Value must be between -1 and 1!")
        result = math.degrees(math.acos(value))
        self.history.append(f"arccos({value}) = {result}°")
        return result
    
    def arctangent(self, value):
        """Arc Tangent (inverse tan)"""
        result = math.degrees(math.atan(value))
        self.history.append(f"arctan({value}) = {result}°")
        return result
    
    # Logarithmic Functions
    def log10(self, a):
        """Logarithm base 10"""
        if a <= 0:
            raise ValueError("Value must be positive!")
        result = math.log10(a)
        self.history.append(f"log10({a}) = {result}")
        return result
    
    def log2(self, a):
        """Logarithm base 2"""
        if a <= 0:
            raise ValueError("Value must be positive!")
        result = math.log2(a)
        self.history.append(f"log2({a}) = {result}")
        return result
    
    def ln(self, a):
        """Natural Logarithm (base e)"""
        if a <= 0:
            raise ValueError("Value must be positive!")
        result = math.log(a)
        self.history.append(f"ln({a}) = {result}")
        return result
    
    def log(self, a, base):
        """Logarithm with custom base"""
        if a <= 0 or base <= 0:
            raise ValueError("Values must be positive!")
        if base == 1:
            raise ValueError("Base cannot be 1!")
        result = math.log(a, base)
        self.history.append(f"log({a}, base={base}) = {result}")
        return result
    
    # Exponential Functions
    def exp(self, a):
        """Exponential (e^x)"""
        result = math.exp(a)
        self.history.append(f"e^{a} = {result}")
        return result
    
    # Absolute Value & Rounding
    def absolute(self, a):
        """Absolute Value"""
        result = abs(a)
        self.history.append(f"|{a}| = {result}")
        return result
    
    def round_num(self, a, decimals=0):
        """Round to specified decimals"""
        result = round(a, decimals)
        self.history.append(f"round({a}, {decimals}) = {result}")
        return result
    
    def floor(self, a):
        """Floor (round down)"""
        result = math.floor(a)
        self.history.append(f"floor({a}) = {result}")
        return result
    
    def ceil(self, a):
        """Ceiling (round up)"""
        result = math.ceil(a)
        self.history.append(f"ceil({a}) = {result}")
        return result
    
    # Statistical Functions
    def factorial(self, n):
        """Factorial (n!)"""
        if n < 0:
            raise ValueError("Factorial not defined for negative numbers!")
        result = math.factorial(int(n))
        self.history.append(f"{n}! = {result}")
        return result
    
    def gcd(self, a, b):
        """Greatest Common Divisor"""
        result = math.gcd(int(a), int(b))
        self.history.append(f"gcd({a}, {b}) = {result}")
        return result
    
    def lcm(self, a, b):
        """Least Common Multiple"""
        result = (int(a) * int(b)) // math.gcd(int(a), int(b))
        self.history.append(f"lcm({a}, {b}) = {result}")
        return result
    
    # Percentage
    def percentage(self, value, percent):
        """Calculate percentage"""
        result = (value * percent) / 100
        self.history.append(f"{percent}% of {value} = {result}")
        return result
    
    def percent_change(self, old_value, new_value):
        """Calculate percentage change"""
        if old_value == 0:
            raise ValueError("Old value cannot be zero!")
        result = ((new_value - old_value) / old_value) * 100
        self.history.append(f"Percent change from {old_value} to {new_value} = {result}%")
        return result
    
    # Complex Number Operations
    def add_complex(self, a, b):
        """Add complex numbers"""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract_complex(self, a, b):
        """Subtract complex numbers"""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply_complex(self, a, b):
        """Multiply complex numbers"""
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide_complex(self, a, b):
        """Divide complex numbers"""
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    # Hyperbolic Functions
    def sinh(self, a):
        """Hyperbolic Sine"""
        result = math.sinh(a)
        self.history.append(f"sinh({a}) = {result}")
        return result
    
    def cosh(self, a):
        """Hyperbolic Cosine"""
        result = math.cosh(a)
        self.history.append(f"cosh({a}) = {result}")
        return result
    
    def tanh(self, a):
        """Hyperbolic Tangent"""
        result = math.tanh(a)
        self.history.append(f"tanh({a}) = {result}")
        return result
    
    # Utility Methods
    def show_history(self):
        """Display calculation history"""
        print("\n" + "="*50)
        print("CALCULATION HISTORY")
        print("="*50)
        if not self.history:
            print("No calculations yet!")
        else:
            for i, calc in enumerate(self.history, 1):
                print(f"{i}. {calc}")
        print("="*50 + "\n")
    
    def clear_history(self):
        """Clear calculation history"""
        self.history = []
        print("History cleared!")
    
    def help_menu(self):
        """Display all available operations"""
        print("\n" + "="*60)
        print("CALCULATOR - AVAILABLE OPERATIONS")
        print("="*60)
        print("\nBASIC OPERATIONS:")
        print("  add(a, b)              - Addition")
        print("  subtract(a, b)         - Subtraction")
        print("  multiply(a, b)         - Multiplication")
        print("  divide(a, b)           - Division")
        print("  floor_divide(a, b)     - Floor Division")
        print("  modulo(a, b)           - Modulo (Remainder)")
        
        print("\nPOWER & ROOT:")
        print("  power(base, exp)       - Power/Exponentiation")
        print("  square(a)              - Square (x^2)")
        print("  cube(a)                - Cube (x^3)")
        print("  square_root(a)         - Square Root")
        print("  cube_root(a)           - Cube Root")
        print("  nth_root(a, n)         - Nth Root")
        
        print("\nTRIGONOMETRIC (angles in degrees):")
        print("  sine(angle)            - Sine")
        print("  cosine(angle)          - Cosine")
        print("  tangent(angle)         - Tangent")
        print("  arcsine(value)         - Arc Sine")
        print("  arccosine(value)       - Arc Cosine")
        print("  arctangent(value)      - Arc Tangent")
        
        print("\nHYPERBOLIC:")
        print("  sinh(a)                - Hyperbolic Sine")
        print("  cosh(a)                - Hyperbolic Cosine")
        print("  tanh(a)                - Hyperbolic Tangent")
        
        print("\nLOGARITHMIC:")
        print("  log10(a)               - Log base 10")
        print("  log2(a)                - Log base 2")
        print("  ln(a)                  - Natural Log (base e)")
        print("  log(a, base)           - Log with custom base")
        print("  exp(a)                 - Exponential (e^x)")
        
        print("\nROUNDING & ABSOLUTE:")
        print("  absolute(a)            - Absolute Value")
        print("  round_num(a, decimals) - Round to decimals")
        print("  floor(a)               - Floor (round down)")
        print("  ceil(a)                - Ceiling (round up)")
        
        print("\nSTATISTICAL:")
        print("  factorial(n)           - Factorial (n!)")
        print("  gcd(a, b)              - Greatest Common Divisor")
        print("  lcm(a, b)              - Least Common Multiple")
        
        print("\nPERCENTAGE:")
        print("  percentage(value, pct) - Calculate percentage")
        print("  percent_change(old, new) - Percentage change")
        
        print("\nCOMPLEX NUMBERS:")
        print("  add_complex(a, b)      - Add complex numbers")
        print("  subtract_complex(a, b) - Subtract complex numbers")
        print("  multiply_complex(a, b) - Multiply complex numbers")
        print("  divide_complex(a, b)   - Divide complex numbers")
        
        print("\nHISTORY:")
        print("  show_history()         - Display all calculations")
        print("  clear_history()        - Clear calculation history")
        print("="*60 + "\n")


# Demo Usage
if __name__ == "__main__":
    calc = Calculator()
    
    # Show help menu
    calc.help_menu()
    
    # Basic Operations Examples
    print("BASIC OPERATIONS EXAMPLES:")
    print(f"10 + 5 = {calc.add(10, 5)}")
    print(f"10 - 5 = {calc.subtract(10, 5)}")
    print(f"10 * 5 = {calc.multiply(10, 5)}")
    print(f"10 / 5 = {calc.divide(10, 5)}")
    print(f"10 % 3 = {calc.modulo(10, 3)}")
    
    # Power & Root Examples
    print("\nPOWER & ROOT EXAMPLES:")
    print(f"2 ** 8 = {calc.power(2, 8)}")
    print(f"5^2 = {calc.square(5)}")
    print(f"√25 = {calc.square_root(25)}")
    print(f"∛27 = {calc.cube_root(27)}")
    
    # Trigonometric Examples
    print("\nTRIGONOMETRIC EXAMPLES:")
    print(f"sin(30°) = {calc.sine(30)}")
    print(f"cos(60°) = {calc.cosine(60)}")
    print(f"tan(45°) = {calc.tangent(45)}")
    
    # Logarithmic Examples
    print("\nLOGARITHMIC EXAMPLES:")
    print(f"log10(100) = {calc.log10(100)}")
    print(f"ln(2.718) ≈ {calc.ln(2.718)}")
    print(f"2^x = 8 → x = {calc.log2(8)}")
    
    # Statistical Examples
    print("\nSTATISTICAL EXAMPLES:")
    print(f"5! = {calc.factorial(5)}")
    print(f"gcd(48, 18) = {calc.gcd(48, 18)}")
    print(f"lcm(12, 18) = {calc.lcm(12, 18)}")
    
    # Percentage Examples
    print("\nPERCENTAGE EXAMPLES:")
    print(f"20% of 100 = {calc.percentage(100, 20)}")
    print(f"Percent change from 50 to 75 = {calc.percent_change(50, 75)}%")
    
    # Complex Numbers
    print("\nCOMPLEX NUMBERS EXAMPLES:")
    print(f"(3+4j) + (1+2j) = {calc.add_complex(3+4j, 1+2j)}")
    print(f"(3+4j) * (1+2j) = {calc.multiply_complex(3+4j, 1+2j)}")
    
    # Show history
    calc.show_history()
