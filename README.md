# 🚀 wsBackend-Fabrica26.1

## 📌 Sobre o projeto

Este projeto é uma aplicação backend desenvolvida com **Django**, que permite:

* Consumir dados da API pública do **Rick and Morty**
* Gerenciar personagens criados pelo usuário (CRUD completo)
* Exibir informações em páginas web simples (HTML + Django Templates)
* Utilizar autenticação com usuários
* Rodar facilmente utilizando **Docker**

---

## 🧩 Funcionalidades

* 🌐 Listagem de personagens (API externa)
* 📺 Listagem de episódios (API externa)
* 🗄️ CRUD de personagens (criar, editar, deletar)
* 🐳 Execução com Docker

---

# ▶️ Como rodar o projeto (passo a passo)

Siga este tutorial simples:

---

## 1️⃣ Baixe o Docker

👉 Instale o Docker Desktop:
https://www.docker.com/products/docker-desktop/

---

## 2️⃣ Abra o terminal na pasta wsBackend-Fabrica26.1

Você pode usar:

* VSCode → `Ctrl + "` 
  ou
* Windows PowerShell

---

## 3️⃣ Crie um usuário administrador

Execute o comando:

```bash
python backend/manage.py createsuperuser
```

Preencha:

* Username
* Email
* Password

---

## 4️⃣ Inicie o servidor com Docker

Copie e cole o comando:

```bash
docker compose up --build
```

---

## 5️⃣ Acesse o projeto

Abra no navegador:

```text
http://127.0.0.1:8000/
```

---

# 📂 Estrutura do projeto

```bash
backend/
├── apps/
│   ├── users/
│   ├── characters/
│   ├── episodes/
├── templates/
├── core/
├── manage.py
```

---

# 🛠️ Tecnologias utilizadas

* Python
* Django
* Django REST Framework
* Docker
* Requests

---

