# Parques-Contagem

O projeto **Parques de Contagem** tem como objetivo apresentar e valorizar os principais parques da cidade de Contagem, Minas Gerais.  
A iniciativa reúne informações sobre a história, estrutura e atrações de locais como o **Parque Fernão Dias**, **Parque Gentil Diniz** e **Parque Ecológico do Eldorado**.

---

## 🔧 Tecnologias Utilizadas

- **Python 3.11** – linguagem principal do projeto  
- **Django 5.2.1** – framework web utilizado no backend  
- **HTML5 & CSS3** – estrutura e estilização das páginas  
- **JavaScript** – interatividade em alguns elementos  
- **Bootstrap** – estilização responsiva  
- **SQLite / PostgreSQL** – bancos de dados utilizados em ambientes de desenvolvimento e produção  
- **Fly.io** – plataforma de hospedagem e deploy da aplicação  
- **Poetry** – ferramenta para gerenciamento de dependências e ambiente virtual  

---

## 📦 Bibliotecas e Ferramentas

### Desenvolvimento e Qualidade de Código
- `pytest` – para testes automatizados  
- `pytest-cov` – medição da cobertura de testes  
- `flake8` – análise estática de código (linting)  

### Configuração e Ambiente
- `python-decouple` – gerenciamento de variáveis de ambiente  
- `dj-database-url` – parse de URLs de banco de dados para o Django  

### Banco de Dados
- `psycopg2-binary` – driver PostgreSQL usado em produção  
- `psycopg` – driver PostgreSQL mais moderno (psycopg3)  

### Armazenamento em Nuvem (S3)
- `boto3` – SDK AWS para comunicação com o S3  
- `django-storages` – integração do Django com serviços de armazenamento como o S3  
- `django-s3-folder-storage` – organização de arquivos em pastas no S3  
- `collectfast` – acelera o processo de coleta de arquivos estáticos no deploy  

### Produção
- `gunicorn` – servidor WSGI usado para servir o Django em produção  
- `sentry-sdk` – monitoramento de erros e exceções em tempo real  

---

## ☁️ Hospedagem

A aplicação está hospedada no [Fly.io](https://fly.io/), que oferece deploys rápidos e escaláveis em nuvem.  
O banco de dados utilizado em produção é o **PostgreSQL**, também configurado via Fly.io.

---

## 📜 Licença

Este projeto está sob a licença MIT.  
Sinta-se à vontade para contribuir, sugerir melhorias ou reportar problemas!

---

**Autor:** Davidson Junio  
📧 [deivisonj1@hotmail.com](mailto:deivisonj1@hotmail.com)
