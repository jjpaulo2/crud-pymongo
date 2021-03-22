FROM python:3.9-buster
LABEL author='João Paulo Carvalho <jjpaulo2@protonmail.com>'

# DEFININDO O DIRETÓRIO PADRÃO DE COMANDOS E O
# LUGAR ONDE SERÁ MONTADO O VOLUME COMPARTILHADO

WORKDIR /crud
VOLUME /crud

# COPIANDO O ARQUIVO `requirements.txt`

COPY requirements.txt requirements.txt

# INSTALANDO AS DEPENDÊNCIAS DO PROJETO

RUN python -m pip install -r requirements.txt

# EXECUTANDO O SERVIDOR UVICORN

CMD python -m pytest