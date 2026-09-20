# tecweb-2026-2-projeto1B
Projeto 1B - André Vasconcellos

Reimplementação do Get-it (Projeto 1) em Django, com banco de dados PostgreSQL e sistema de tags (many-to-many).

## Link da aplicação em produção

https://tecweb-2026-2-projeto1b-kuzm.onrender.com

## Funcionalidades

- CRUD de notas (criar, listar, editar, excluir)
- Cada nota pode ter várias tags, uma só, ou nenhuma (relação many-to-many)
- Página com a lista de todas as tags (`/tags/`)
- Página de detalhe de uma tag, com as notas associadas a ela (`/tags/<id>/`)

