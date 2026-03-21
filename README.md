# 🚀 wsBackend-Fabrica26.1

## 📌 Sobre o projeto

Este projeto é uma aplicação web desenvolvida com **Django** que funciona como um backend completo, capaz de:

Gerenciar dados internos (usuários, personagens e episódios)

Consumir dados de uma API externa (Rick and Morty API)

Exibir informações em páginas web simples

Disponibilizar dados via API (REST)

---

## 🧩 Funcionalidades

### ✔ CRUD completo

O sistema permite:

Criar

Listar

Atualizar

Deletar
 
Entidades:

Personagens

Episódios

---

### ✔ Integração com API externa

O projeto consome dados da API pública de Rick and Morty (https://rickandmortyapi.com/api/character/ e https://rickandmortyapi.com/api/location), permitindo:

Listar personagens

Listar episódios

---

### ✔ Interface web

Possui páginas simples com HTML + Django Templates:

Página inicial (Home)

Lista de personagens

Lista de episódios

---

### ✔ Autenticação

Sistema de usuários

Base para autenticação via token

---

### ✔ Docker

O projeto pode ser executado facilmente usando Docker, sem precisar instalar dependências manualmente.

---

## 🛠️ Tecnologias utilizadas

Python

Django

Django REST Framework

Requests (para consumir API externa)

Docker

---

# ▶️ Como rodar o projeto (forma simples)

## 🔹 Pré-requisitos

Você precisa ter instalado:

Python (versão 3.10 ou superior)

Docker (opcional, mas recomendado)

---

# 🥈 Rodando com Docker (recomendado)

## 1. Build da imagem

docker build -t wsbackend .
```

---

## 2. Rodar o container

docker run -p 8000:8000 wsbackend
```

---

## 3. Acessar no navegador

```text
http://localhost:8000/
```

---
