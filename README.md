# tecweb-2026-2-projeto1B
Projeto 1B - André Vasconcellos

Reimplementação do Get-it (Projeto 1) em Django, com banco de dados PostgreSQL e sistema de tags.

## Link da aplicação em produção

   https://tecweb-2026-2-projeto1b-kuzm.onrender.com
   
## Funcionalidades

- CRUD de notas (criar, listar, editar, excluir)
- Cada nota pode ter uma tag (opcional)
- Página com a lista de todas as tags (`/tags/`)
- Página de detalhe de uma tag, com as notas associadas a ela (`/tags/<id>/`)

## Rodando localmente

1. Suba um Postgres via Docker (veja o handout de Containers e Bancos de Dados da disciplina) e crie o banco/usuário `getit` / `getituser` / `getitsenha`, ou defina a variável de ambiente `DATABASE_URL` apontando para o seu Postgres.
2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
3. Rode as migrações e o servidor:
   ```
   python manage.py migrate
   python manage.py runserver
   ```
4. Acesse `http://localhost:8000/`.
