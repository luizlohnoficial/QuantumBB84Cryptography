
# Retona string de chave simétrica de 8 bits
def DescriptografaCaracter(c, key):
    d = (int(c, 2) - int(key, 2)) % 255
    return chr(d)


# Descriptografa mesagem de acordo com o método de chave única usado
def DescriptografaMensagem(msgs, keys):
    Msg_Cript = []
    for i in range(len(msgs)):
        Msg_Cript.append(DescriptografaCaracter(msgs[i], keys[i]))
    Msg_Cript = "".join(Msg_Cript)
    return Msg_Cript
