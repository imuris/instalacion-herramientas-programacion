salario_bruto = float(input("Ingresa el salario bruto mensual: "))
porcentaje_impuestos = float(input("Ingresa el porcentaje de impuestos: "))
deducciones = float(input("Ingresa las deducciones adicionales: "))

impuesto = salario_bruto * (porcentaje_impuestos / 100)

salario_neto = salario_bruto - impuesto - deducciones

print("El impuesto es:", impuesto)
print("El salario neto es:", salario_neto)