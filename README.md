![](https://img.shields.io/badge/Status%20de%20Desenvolvimento%3A-Inicial%3A%20Em%20Desenvolvimento-orange?style=for-the-badge&labelColor=red)

Essa documentação ainda não está finalizada. Como o projeto ainda está em desenvolvimento, algumas informações poderão ser alteradas.

**Status BackEnd:** Iniciado

**Status FrontEnd:** Não iniciado

# 📒 My Books Manager

O intuito desse projeto é criar uma aplicação web de um gerenciador de livros simples, onde o usuário poderá buscar livros, adicioná-los a sua lista de leituras, lista de livros para ler ou livros lidos. 

*A inspiração para esse projeto é o app [Skoob](https://www.skoob.com.br/)*

## 🚀 Tecnologias Utilizadas

- **Python** — Linguagem de desenvolvimento da API.
	- FastAPI;
	- SQLAlchemy;
	- Pydantic.
- **Vue** — Framework de desenvolvimento do FrontEnd.
	- VueRouter
	- Pinia
- **Docker** — Facilita a criação e execução de ambientes isolados, garantindo que o projeto rode da mesma forma em qualquer máquina.
- **PostgreSQL** — Banco de dados.


## ⚙️ Como o Projeto Foi Construído

O projeto foi estruturado para priorizar organização e escalabilidade. Os principais pontos de arquitetura são:

- **Separação de responsabilidades:** código dividido em módulos para facilitar manutenção e testes.
- **Automação de tarefas:** uso de Makefile para comandos comuns.
- **Ambiente isolado:** configuração de Docker para evitar problemas de dependências.

## 🛠️ Como Rodar o Projeto

### Informações iniciais:

 - **Portas:**
	- A aplicação utilizará as portas locais 8080, 8000, 5432 para rodar, respectivamente, a plataforma, o servidor da API e o banco de dados. Então garanta que as essas portas não estão sendo utilizadas.
 - **Dependências:**
	- Node (versão utilizada: 22.16.0)
	- Python (versão utilizada 3.9.16)
	- Gerenciadores de pacotes para Python e Node (os utilizados foram PIP e Yarn/NPM)
	- Banco de dados PostgreSQL (versão utilizada 17.6)

Você pode rodar o projeto de duas maneiras: utilizando Docker (recomendado) ou diretamente na sua máquina local.

### 1. Utilizando Docker

1. **Certifique-se de ter o Docker instalado.**
2. No terminal, acesse o diretório do projeto.
3. Definir as variáveis de ambientes

	3.1. Criar um arquivo .env com as variáveis de ambiente necessárias

	O arquivo `.env.example` contém as variáveis necessárias

4. Execute:

   ```bash
   docker-compose up -d
   ```

- **Aplicação:** http://localhost:8080/
- **API:** http://localhost:8000

### 2. Utilizando sem Docker

1. **Certifique-se de ter Python 3.9.16 instalado.**
2. Definir as variáveis de ambientes

	2.1. Criar um arquivo .env com as variáveis de ambiente necessárias

	O arquivo `.env.example` contém as variáveis necessárias

3. **Na raiz da pasta `backend`**, crie um ambiente virtual (nesse caso utilizei o venv):
   ```bash
   python -m venv venv
   ```

	 3.1. Ative o ambiente virtual
	 ```bash
	./venv/scripts/activate
	 ```

4. Instale as dependências rodando:
   ```bash
   make install
   ```
	 e
	 
   ```bash
   make install-dev
   ```

5. Para rodar a aplicação:

   ```bash
   make run-api
   ```

4. Para executar os testes:

   ```bash
   make test
   ```

5. **Na raiz da pasta `frontend`**, instale as dependências rodando:

   ```bash
   yarn
   ```
	 ou

   ```bash
   npm i
   ```

2. Rode o frontend:

	```bash
	yarn dev
	```
	ou

	```bash
	npm run dev
	```

## 📚 Funcionalidades Principais

- Usuários:
	- Cadastro;
	- Autenticação;
	- Listagem de informações;
	- Atualização de informações.
- Livros:
	- Consulta por titulo, autor, isbn..
	- Cadastro, edição e remoção.
- Livros do usuário:
	- Cadastro, listagem, edição e remoção de livros;
	- Criação de anotações;
	- Marcação como lidos, lendo e para ler;
	- Possibilidade de dar notas (1 a 5)

---

> Desenvolvido por [gisela-mariano](https://github.com/gisela-mariano)