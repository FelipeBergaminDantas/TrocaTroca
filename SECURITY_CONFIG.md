# Segurança e Configuração do Projeto TrocaTroca

## Objetivo

Esta melhoria foi aplicada para fortalecer a segurança da API e deixar a configuração do projeto mais profissional, previsível e pronta para ambientes reais de desenvolvimento e produção.

## O que foi melhorado

### 1) Secret key controlada por ambiente
Antes, a aplicação usava uma chave padrão fixa em código, o que é inseguro e inadequado para produção.

Agora a aplicação lê a variável de ambiente `SECRET_KEY` e exige que ela exista quando o ambiente for `production`.

Exemplo:

```bash
set APP_ENV=production
set SECRET_KEY=sua_chave_muito_segura_aqui
```

Em desenvolvimento, o sistema ainda aceita um valor padrão local para facilitar o uso inicial, mas a configuração real deve ser externizada para o ambiente.

### 2) Controle de debug por variável de ambiente
A execução da API agora usa as variáveis:

- `DEBUG`
- `HOST`
- `PORT`

Isso evita que a aplicação rode em modo de depuração por padrão em produção.

Exemplo:

```bash
set DEBUG=false
set HOST=0.0.0.0
set PORT=5000
```

### 3) CORS configurado por ambiente
Antes, o backend liberava todas as origens com `*` em todas as requisições da API. Isso pode ser aceitável em ambiente local, mas é ruim em produção.

Agora a origem permitida pode ser configurada pela variável `CORS_ALLOWED_ORIGINS`.

Exemplo:

```bash
set CORS_ALLOWED_ORIGINS=http://localhost:5500,http://127.0.0.1:5500
```

Também é possível usar `*` apenas em ambiente de desenvolvimento, quando necessário.

### 4) Cabeçalhos de segurança adicionados
A API agora envia headers básicos de segurança para reduzir riscos comuns:

- `X-Content-Type-Options: nosniff`
- `X-Frame-Options: SAMEORIGIN`
- `Referrer-Policy: strict-origin-when-cross-origin`

Esses headers ajudam a evitar alguns tipos de abuso e melhoram o comportamento da aplicação em navegadores modernos.

### 5) Configuração do banco via ambiente
A URL do banco continua configurável pela variável `DATABASE_URL`, mantendo flexibilidade para uso com SQLite em desenvolvimento e PostgreSQL em produção.

Exemplo:

```bash
set DATABASE_URL=sqlite:///trocatroca.db
```

ou em produção:

```bash
set DATABASE_URL=postgresql://usuario:senha@host:5432/trocatroca
```

---

## Como usar no projeto

Para rodar localmente:

```bash
set APP_ENV=development
set DEBUG=true
set SECRET_KEY=troca-troca-chave-local
set CORS_ALLOWED_ORIGINS=*
python run.py
```

Para ambiente de produção, o ideal é:

```bash
set APP_ENV=production
set DEBUG=false
set SECRET_KEY=sua_chave_gerada_com_segurança
set CORS_ALLOWED_ORIGINS=https://seu-front.com
set DATABASE_URL=postgresql://usuario:senha@host:5432/trocatroca
python run.py
```

## Benefícios da mudança

- reduz risco de vazamento de segredos;
- deixa a aplicação mais segura em produção;
- facilita a configuração em diferentes ambientes;
- melhora a gestão de deploy e integração com frontend/backend;
- cria uma base mais profissional para evolução do projeto.

## Resumo

A aplicação passou a seguir um padrão mais seguro e mais fácil de configurar, sem quebrar o ambiente local de desenvolvimento. O foco principal foi remover valores sensíveis fixos no código e deixar as configurações explícitas por variável de ambiente.
