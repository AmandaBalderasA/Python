ipi = float(input("Ingrese cantidad: "))
if ipi < 85528:
    tax = (ipi*0.18) - 556.02
else:
    tax = (ipi - 85528) * 0.32 + 14839.02

if ipi <= 0.0:
    tax = 0.0

print("El impuesto es: ", round(tax,0))
