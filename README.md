# 🚀 wsBackend-Fabrica26.1

## 📌 Sobre o projeto

Este projeto é uma aplicação web desenvolvida com **Django**, funcionando como um backend completo capaz de:

* 🔧 Gerenciar dados internos (**usuários, personagens e episódios**)
* 🌐 Consumir dados de uma API externa (**Rick and Morty API**)
* 🖥️ Exibir informações em páginas web simples
* 🔌 Disponibilizar dados via API (**REST**)

---

## 🧩 Funcionalidades

### ✔ CRUD completo

O sistema permite realizar operações completas de:

* ➕ Criar
* 📄 Listar
* ✏️ Atualizar
* ❌ Deletar

📦 **Entidades gerenciadas:**

* Personagens
* Episódios

---

### ✔ Integração com API externa

O projeto consome dados da API pública **Rick and Morty**, permitindo:

* 👤 Listar personagens
* 🎬 Listar episódios

🔗 Endpoints utilizados:

* https://rickandmortyapi.com/api/character/
* https://rickandmortyapi.com/api/location

---

### ✔ Interface web

Interface simples utilizando **HTML + Django Templates**:

* 🏠 Página inicial (Home)
* 👥 Lista de personagens
* 🎞️ Lista de episódios

---

### ✔ Autenticação

* 👤 Sistema de usuários
* 🔐 Base preparada para autenticação via **token**

---

### ✔ Docker

O projeto pode ser executado facilmente com **Docker**, sem necessidade de instalar dependências manualmente.

---

## 🛠️ Tecnologias utilizadas

* 🐍 Python
* 🌐 Django
* 🔌 Django REST Framework
* 📡 Requests (consumo de API externa)
* 🐳 Docker

---

# ▶️ Como rodar o projeto

## 🔹 Pré-requisitos

Você precisa ter instalado:

* Python **3.10+**
* Docker *(opcional, mas recomendado)*

---

## 🥈 Rodando com Docker

### 1️⃣ Build da imagem

```bash
docker build -t wsbackend .
```

---

### 2️⃣ Rodar o container

```bash
docker run -p 8000:8000 wsbackend
```

---

### 3️⃣ Acessar no navegador

```text
http://localhost:8000/
```

---

## 💡 Dica

Se quiser rodar sem Docker, você pode:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---


