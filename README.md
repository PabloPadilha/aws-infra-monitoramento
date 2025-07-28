# aws-infra-monitoramento:
Monitoramento de EC2 com Python e boto3 em ambiente WSL.


Este projeto tem como objetivo monitorar e interagir com recursos da AWS usando Python e a biblioteca `boto3`, simulando um cenário real de atuação como analista de suporte em nuvem.

## Funcionalidades:

- Monitoramento de instâncias EC2:
  - Consulta de estado (`running`, `stopped`)
  - Listagem de IDs e informações básicas

- Integração com AWS CLI e boto3 para acesso programático

- Ambiente configurado em **WSL (Ubuntu no Windows)** com virtualenv e acesso SSH à instância EC2

## Estrutura do Projeto:

aws-monitoramento/
├── aws-key.pem # Chave de acesso à EC2
├── ec2_status.py # Script Python para listar status das instâncias
├── venv/ # Ambiente virtual Python
└── README.md

## Pré-requisitos:

- Conta AWS com IAM configurado (Access Key+Secret)
- Instância EC2 já criada
- AWS CLI e boto3 instalados no ambiente Linux (WSL recomendado)
- Python 3.10 ou superior (no WSL)

## Passo a Passo:

No WSL:
  Criar e ativar ambiente virtual:
  python3 -m venv venv
  source venv/bin/activate

  Instalar dependências:
  pip install boto3 awscli

  Configurar aws CLI:
  aws configure

  Executar o script:
  python ec2_status.py



