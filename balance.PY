from sympy import symbols, Eq, solve

def balance_combustion(formula):
    # Elementos involucrados en la combustión
    C, H, O = symbols('C H O')
    
    # Extraer cantidad de átomos de C e H en el hidrocarburo
    import re
    match = re.match(r'C(\d*)H(\d*)', formula)
    if not match:
        return "Fórmula inválida. Use formato como 'C2H6'"
    
    nC = int(match.group(1)) if match.group(1) else 1
    nH = int(match.group(2)) if match.group(2) else 1
    
    # Definir coeficientes desconocidos
    a, b, c, d = symbols('a b c d')
    
    # Ecuaciones de balance
    eq1 = Eq(nC * a, c)  # Carbono
    eq2 = Eq(nH * a, 2 * d)  # Hidrógeno
    eq3 = Eq(2 * b, 2 * c + d)  # Oxígeno
    
    # Resolver ecuaciones
    solution = solve((eq1, eq2, eq3), (a, b, c, d))
    
    if solution:
        return f"{solution[a]} {formula} + {solution[b]} O2 -> {solution[c]} CO2 + {solution[d]} H2O"
    else:
        return "No se pudo balancear la ecuación."

# Ejemplo de uso
if __name__ == "__main__":
    hidrocarburo = input("Ingrese la fórmula del hidrocarburo (ej. C2H6): ")
    print(balance_combustion(hidrocarburo))
