# QuantumBB84Cryptography

Este projeto demonstra uma implementação didática do protocolo BB84 em Python
e Q#. Para executar o script principal é possível fornecer a senha por meio da
variável de ambiente `PASSWORD` ou digitá-la manualmente.

```bash
# Exemplo utilizando variável de ambiente
PASSWORD=MinhaSenha python start.py
```

Caso o pacote `qsharp` não esteja disponível (por exemplo em ambientes sem
acesso à internet), a implementação em `criptografar.py` utiliza um modo de
simulação em Python para gerar as chaves aleatórias.
