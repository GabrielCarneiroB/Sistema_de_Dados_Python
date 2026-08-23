print("\n------------------------")
print("       CABEÇALHO        ")
print("------------------------")

#Criando um dicionário
aluno = {
    "nome": "Gabriel C Barros ", "disciplina": "Python intermediario", "nota": "8"

}
#Usando as F-strings e acessando as chaves do dicionário
#
print(f" 👩🏻‍🦰 Aluno(a):{aluno['nome']}")
print(f" 📚 Disciplina: {aluno['disciplina']}")
print(f" 💸 Nota: {aluno['nota']}")


from datetime import datetime
data_formada = datetime.now().strftime("%d/%m/%Y")

#Usando f-string para juntar o texto com a variável
print(f" 📅 Data{data_formada}")
#Saída: Data 16/06/2026
print("-------------------------------")


# Codificando no PyCharm

print("=== SISTEMA DE HIGIENIZAÇÃO DE DADOS ===")

# 1. Criando uma lista de cadastros que possui elementos duplicados
lista_suja = ["Ana", "Carlos", "Ana", "Beatriz", "Carlos"]

# Convertendo para Set (Conjunto) para eliminar duplicados automaticamente!
conjunto_limpo = set(lista_suja)

print(f"Lista original (com duplicados): {lista_suja}")
print(f"Conjunto final (Sets removem duplicados): {conjunto_limpo}\n")

# 2. Protegendo o código contra erros com Try / Except
try:
    # Se o usuário digitar letras ou o número zero, o programa não travará!
    numero = int(input("Digite um número inteiro divisor de 100: "))
    resultado = 100 / numero
    print(f"Sucesso! O resultado da divisão de 100 por {numero} é {resultado:.2f}")

except ZeroDivisionError:
    print("❎️ Erro: Não é possível dividir um número por ZERO!")

except ValueError:
    print("❎️ Erro: Por favor, digite apenas números inteiros válidos!")

except Exception as erro_inesperado:
    print(f"❎️ Ocorreu um erro desconhecido: {erro_inesperado}")

finally:
    print("\nExecução da análise segura finalizada com sucesso.")
    print("===============================================")
