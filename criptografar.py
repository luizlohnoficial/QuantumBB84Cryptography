# Importando bibliotecas necessárias
import random
import logging

logger = logging.getLogger(__name__)

try:
    import qsharp  # opcional para execuções reais em Q#
    from CriptBB84 import KeyBB84, RandomBit
    HAS_QSHARP = True
except Exception:  # ambiente sem dependências do Q# ou falha ao compilar
    HAS_QSHARP = False


def GenerateRandonBits(n):
    vetor = []
    for i in range(n):
        vetor.append(random.randint(0, 1))
    return vetor


# Retorna vetor de n bits aleatórios com Q#
# range: retorna uma sequência de números *
# simulate irá simular a execução da função GenerateRandonBits
def QubitsRandonBits(n):
    """Retorna um vetor de bits aleatórios.

    Quando a dependência qsharp está disponível, utiliza as simulações em Q#.
    Caso contrário, gera bits pseudoaleatórios em Python para fins de teste.
    """
    vetor = []
    for _ in range(n):
        if HAS_QSHARP:
            vetor.append(RandomBit.simulate())
        else:
            vetor.append(random.randint(0, 1))
    return vetor


def GeraChaveCompartilhada():
    """Gera uma chave compartilhada simulando o protocolo BB84."""
    if HAS_QSHARP:
        key = []  # vetor inicial
        while len(key) <= 8:  # necessário 8 bits para representar qualquer valor da ASCII
            tam = 16
            UserOrigen = QubitsRandonBits(tam)
            UserOrigenBase = QubitsRandonBits(tam)
            UserDestinoBase = QubitsRandonBits(tam)

            logger.debug("UserOrigen     : %s", UserOrigen)
            logger.debug("UserOrigenBase : %s", UserOrigenBase)
            logger.debug("UserDestinoBase: %s", UserDestinoBase)

            key = KeyBB84.simulate(
                AliceBits=UserOrigen,
                AliceBase=UserOrigenBase,
                BobBase=UserDestinoBase,
                n=tam,
            )
            logger.debug("key sendo unida: %s", key)

        key = [str(i) for i in key]
        key = "".join(key)
        logger.debug("key apenas converter lista: %s", key)
        return key
    else:
        # Sem suporte a Q#, gera uma chave de 8 bits pseudoaleatória
        chave_bits = GenerateRandonBits(8)
        return "".join(str(b) for b in chave_bits)


def CriptografaCaracter(c, key):
    logger.debug("C ORD: %s", ord(c))
    logger.debug("int(key, 2) % 255: %s", int(key, 2) % 255)

    c = (ord(c) + int(key, 2)) % 255
    logger.debug("criptografa caractere: %s", c)
    logger.debug("bin: %s", bin(c))

    return bin(c)


# Usar qualquer método de criptografia de chave única
def CriptografaMensagem(SenhaFornecida):
    Msg_Cript = []
    Keys = []
    for i in SenhaFornecida:
        key = GeraChaveCompartilhada()
        Keys.append(key)
        Msg_Cript.append(CriptografaCaracter(i, key))
        logger.debug("CriptografaMensagemKey: %s", key)
        logger.debug("CriptografaMensagemMSG: %s", Msg_Cript)
    return (Msg_Cript, Keys)
