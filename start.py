# Importando bibliotecas necessárias
import os
import sys
import logging
import criptografar
import descriptografar

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

logger.info("Iniciando processo de criptografia")
password = "Login123"
if password:
    logger.info("Senha obtida da variável de ambiente")
else:
    if sys.stdin.isatty():
        logger.info("Solicitando senha ao usuário")
        try:
            password = input("Digite uma palavra para enviar: ")
        except EOFError:
            logger.error("Nenhuma senha fornecida")
            raise SystemExit("Nenhuma senha fornecida")
    else:
        logger.error("Variável PASSWORD não definida e sem entrada interativa")
        raise SystemExit("Nenhuma senha fornecida")

# remove aspas extras e quebras de linha caso venham de variáveis de ambiente
password = password.strip().strip('"').strip("'")

logger.info("Mensagem recebida: %s", SenhaFornecida)
logger.info("Chaves: %s", keys)
logger.info("Msg Criptografada: %s", Msg_Cript)
logger.info("Msg Descriptografada: %s", Msg_Descript)

# Criptografa usando OTP para cada caracter
Msg_Cript, keys = criptografar.CriptografaMensagem(SenhaFornecida)
print(f"Chaves: {keys}")
print(f"Msg Criptografada: {Msg_Cript}")

# Descriptografa usando chave única
Msg_Descript = descriptografar.DescriptografaMensagem(Msg_Cript, keys)
print(f"Msg Descriptografada: {Msg_Descript}")
