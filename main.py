import tkinter as tk
from tkinter import messagebox
from sympy import symbols, diff
from sympy.parsing.sympy_parser import parse_expr
import re


class DifferentiationCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Differentiation Solving Calculator")
        self.create_widgets()

    def create_widgets(self):
        # Function Input
        tk.Label(self.root, text="Function:").grid(row=0, column=0, padx=10, pady=5)
        self.func_entry = tk.Entry(self.root, width=50)
        self.func_entry.grid(row=0, column=1, padx=10, pady=5)

        # Variable Input
        tk.Label(self.root, text="Variable:").grid(row=1, column=0, padx=10, pady=5)
        self.var_entry = tk.Entry(self.root, width=10)
        self.var_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Order of Differentiation
        tk.Label(self.root, text="Order:").grid(row=2, column=0, padx=10, pady=5)
        self.order_entry = tk.Entry(self.root, width=10)
        self.order_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Compute Button
        self.compute_button = tk.Button(self.root, text="Compute Derivative", command=self.compute_derivative)
        self.compute_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Result Display
        tk.Label(self.root, text="Result:").grid(row=4, column=0, padx=10, pady=5)
        self.result_text = tk.Text(self.root, height=10, width=65)  # Increased height
        self.result_text.grid(row=4, column=1, padx=10, pady=5)

        # Clear Button
        self.clear_button = tk.Button(self.root, text="Clear", command=self.clear_inputs)
        self.clear_button.grid(row=5, column=0, columnspan=2, pady=10)

    def validate_input(self, func_str, var_str, order_str):
        if not func_str:
            raise ValueError("Function cannot be empty.")

        if not var_str:
            raise ValueError("Variable cannot be empty.")

        if not re.match(r'^[a-zA-Z]$', var_str):
            raise ValueError("Variable must be a single letter.")

        try:
            order = int(order_str)
            if order < 1:
                raise ValueError("Order must be a positive integer.")
        except ValueError:
            raise ValueError("Order must be a positive integer.")

        return func_str, var_str, order

    def compute_derivative(self):
        self.result_text.delete("1.0", tk.END)
        try:
            func_str = self.func_entry.get().strip()
            var_str = self.var_entry.get().strip()
            order_str = self.order_entry.get().strip()

            func_str, var_str, order = self.validate_input(func_str, var_str, order_str)

            var = symbols(var_str)
            func = parse_expr(func_str)

            derivative = diff(func, var, order)

            self.result_text.insert(tk.END,
                                    f"The {order}-order derivative of {func_str} with respect to {var_str} is:\n{derivative}")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clear_inputs(self):
        self.func_entry.delete(0, tk.END)
        self.var_entry.delete(0, tk.END)
        self.order_entry.delete(0, tk.END)
        self.result_text.delete("1.0", tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = DifferentiationCalculator(root)
    root.mainloop()
