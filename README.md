# aws-infra-monitoramento:
Monitoramento de EC2 e RDS com Python e boto3 em ambiente WSL.


Este projeto tem como objetivo monitorar e interagir com recursos da AWS usando Python e a biblioteca `boto3`, simulando um cenário real de atuação como analista de suporte em nuvem.

## Funcionalidades:

- Monitoramento de instâncias EC2:
  - Consulta de estado (`running`, `stopped`)
  - Listagem de IDs e informações básicas

- Monitoramento de instâncias RDS:
  - Configuração de instância RDS com MySQL.
  - Permissões de acesso e regras de segurança revisadas.
  - Teste de conexão via terminal (WSL) com o comando:


- Integração com AWS CLI e boto3 para acesso programático
- Ambiente configurado em **WSL (Ubuntu no Windows)** com virtualenv e acesso SSH à instância EC2

## Estrutura do Projeto:

aws-monitoramento/
├── aws-key.pem # Chave de acesso à EC2
├── ec2_status.py # Script Python para listar status das instâncias
├── venv/ # Ambiente virtual Python
└── README.md

aws-monitoramento/
├── backup_rds.py         # Script para snapshot automático do RDS
├── requirements.txt      # APENAS SE DESEJAR, porém desejável para boas práticas
├── README.md             # Documentação do projeto
└── (venv/)               # Ambiente virtual Python


## Pré-requisitos:

EC2:
  - Conta AWS com IAM configurado (Access Key+Secret)
  - Instância EC2 já criada
  - AWS CLI e boto3 instalados no ambiente Linux (WSL recomendado)
  - Python 3.10 ou superior (no WSL)

RDS:
  - Conta AWS com permissões para EC2, RDS e IAM.  
  - Chave de acesso IAM configurada no aws configure.  
  - Python 3.12 com boto3 instalado.  
  - Conexão com a internet e terminal (WSL, Linux ou Mac).

## Passo a Passo:

No WSL:
  EC2:
    Criar e ativar ambiente virtual:
    python3 -m venv venv
    source venv/bin/activate
  
    Instalar dependências:
    pip install boto3 awscli
  
    Configurar aws CLI:
    aws configure
  
    Executar o script:
    python ec2_status.py

  RDS:
    comando bash para conectar: mysql -h <endpoint> -u <usuario> -p
    explicação:
      mysql = programa;
      h = host;
      u = usuário;
      p = password;

   

    



