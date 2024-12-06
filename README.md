* * *

**Teste para desenvolvedor - Matemática**

"Uma aplicação para realizar operações matemáticas protegidas por autenticação JWT, com um frontend em React e backend em FastAPI, utilizando Docker para orquestração.

* * *

## **Índice**

1. [Introdução](#introdu%C3%A7%C3%A3o)
2. [Tecnologias Utilizadas](#tecnologias-utilizadas)
3. [Pré-requisitos](#pr%C3%A9-requisitos)
4. [Configuração e Execução](#configura%C3%A7%C3%A3o-e-execu%C3%A7%C3%A3o)
5. [Uso](#uso)
6. [Contribuições](#contribui%C3%A7%C3%B5es)
7. [Licença](#licen%C3%A7a)

* * *

## **1. Introdução**

Este projeto foi desenvolvido como parte de um desafio técnico para criar uma API segura que realiza operações matemáticas e um frontend que consome essa API

* * *

## **2. Tecnologias Utilizadas**

* **Frontend:** React
* **Backend:** FastAPI
* **Autenticação:** JWT (JSON Web Tokens)
* **Orquestração:** Docker, Docker-Compose

* * *

## **3. Pré-requisitos**

* Docker e Docker-Compose instalados ([guia oficial](https://docs.docker.com/get-docker/))
* Node.js instalado para o frontend ([guia oficial](https://nodejs.org/))
* Postman (ou ferramenta similar) para testes de API (opcional).

* * *

## **4. Configuração e Execução**

### **4.1. Clone o repositório**

    git clone https://github.com/MonariAndre/Matematica
    cd Matematica

### **4.2. Suba os containers com Docker**

    docker-compose up --build

### **4.3. Acesse o frontend**

* Abra o navegador e acesse: `http://localhost:3000`

### **4.4. Teste a API (opcional)**

* Acesse: `http://localhost:8000/docs` para a documentação gerada automaticamente pelo FastAPI.

* * *

## **5. Uso**

Mostre como usar o sistema, com exemplos claros:

* **Tela de Login:** informe o username `admin` e password `password` para se autenticar.
* **Operações Matemáticas:** insira dois números e escolha a operação desejada.

## Fornecer endpoints da API: 
    
### Obter token POST http://localhost:8000/token

#### Body mode: x-www-from-urlendcode

    { 
        "username": "admin", 
        "password": "password" 
    }

#### Reponse Body (exemplo):   

    {
        "access_token": <seu-token>,    
        "token_type": "bearer"
    }
   
### Realizar operação matemática POST http://localhost:8000/calculate 
#### Authorization: 
Auth type: "Bearer Token": < seu-token > <br/>
Body mode raw:

    {
        "num1": 10, 
        "num2": 5, 
        "operation": "add" 
    }

#### Reponse Body (exemplo):

    {
        "result": 15.0   
    }

* * *

## **6. Contribuições**

Você pode contribuir com o projeto da seguinte forma:

* Faça um fork do repositório
* Crie uma branch para sua feature/correção
* Abra um pull request com uma descrição clara das mudanças.

* * *

## **7. Licença**

Este projeto é licenciado sob a MIT License.

* * *