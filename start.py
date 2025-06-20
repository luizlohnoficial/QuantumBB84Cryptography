# Importando bibliotecas necessárias
import os
import criptografar
import descriptografar

if not password:
    try:
        password = input("Digite uma palavra para enviar: ")
    except EOFError:
        raise SystemExit("Nenhuma senha fornecida")

# remove aspas extras e quebras de linha caso venham de variáveis de ambiente
password = password.strip().strip('"').strip("'")

if password is None:
    password = input("Digite uma palavra para enviar: ")
SenhaFornecida = password
print(f"Mensagem: {SenhaFornecida}")

# Criptografa usando OTP para cada caracter
Msg_Cript, keys = criptografar.CriptografaMensagem(SenhaFornecida)
print(f"Chaves: {keys}")
print(f"Msg Criptografada: {Msg_Cript}")

# Descriptografa usando chave única
Msg_Descript = descriptografar.DescriptografaMensagem(Msg_Cript, keys)
print(f"Msg Descriptografada: {Msg_Descript}")
