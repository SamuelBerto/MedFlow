# 🏥 MedFlow
---
Sistema de gerenciamento de saúde desenvolvido em Python com arquitetura modular, banco de dados SQLite e operações CRUD completas.


## 🛠️ Tecnologias utilizadas
---
- Python
- SQLite
- SQL
- Git/GitHub


## 🎞️ Versão atual do Projeto em GIF. 
---
V.3
<img width="1152" height="648" alt="medflowGIFV3" src="https://github.com/user-attachments/assets/4877aff0-d212-48a7-ae9b-4f737c7fff2b" />


## ✨ Funcionalidades

### 👤 Pacientes
- Cadastro de pacientes
- Listagem de pacientes
- Edição de pacientes
- Remoção de pacientes
  
### 👨‍⚕️ Médicos
- Cadastro de médicos
- Listagem de médicos
- Edição de médicos
- Remoção de médicos

### 📅 Consultas
- Agendamento de consultas
- Listagem de consultas
- Edição de consultas
- Cancelamento de consultas

### 🛡️ Validações
- Verificação de IDs válidos
- Campos obrigatórios
- Validação de entradas

## 🖼️ Evolução do Projeto em GIF.
---

V.1
<img width="1152" height="648" alt="medflowGIFV1" src="https://github.com/user-attachments/assets/cfbf1ecd-6b83-4824-97cf-3e0aaa5fb951" />

---
V.2
<img width="1152" height="648" alt="medflowGIFV2" src="https://github.com/user-attachments/assets/1b720d49-ea6f-4fef-9081-7279a3407e43" />



## 📚 Objetivo do projeto
---
Projeto criado para praticar:
- Python
- SQL
- APIs
- Arquitetura de software
- Desenvolvimento visual
- Boas práticas de desenvolvimento
- Boas práticas de GitHub-Commits, merges, branches.


## 🚧 Próximas melhorias
---

- API Flask
- Interface web
- Sistema de login
- Dashboard administrativo



## 🔧 Estrutura do projeto
---

```bash
MedFlow/
│
├── database/
│       └─ conexao.py
│
├── models/
├── services
│       ├─ consulta_service.py
│       ├─ medico_service.py
│       └─ paciente_service.py
│
├── static/
│       └─ style.css
│
├── templates/
│       ├─ index.html
│       ├─ pacientes.html
│       ├─ medicos.html
│       ├─ consultas.html
│       ├─ novo_paciente.html
│       ├─ novo_medico.html
│       ├─ nova_consulta.html
│       ├─ editar_paciente.html
│       ├─ editar_medico.html
│       └─ editar_consulta.html
│
├── utils/
│       └─ menu.py
├── main.py
├── app.py
├── medflow.db
├── LICENSE
├── requirements.txt
├── .gitattributes
├── .gitgnore
└─ ─README.md

```


## ▶️ Como executar
---

```bash
python main.py
python app.py

```


## 👨‍💻 Autor
---
Desenvolvido por Samuel Berto.
