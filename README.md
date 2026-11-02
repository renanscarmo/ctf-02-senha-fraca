# CTF 02: Senha Fraca

Projeto criado a partir do [template-seguranca](https://github.com/renanscarmo/template-seguranca)
para praticar segurança em Python.

## Objetivo

Entrar na área restrita adivinhando a senha do administrador e depois corrigir a falha.

## Como foi

1. **Antes:** a senha ficava escrita no código (`admin123`). O ataque foi testar senhas comuns e funcionou.
2. **Detecção:** o Bandit acusou a senha no código (B105) e o pipeline ficou vermelho.
3. **Depois:** o código guarda só o hash da senha, lido de uma variável de ambiente. O pipeline ficou verde.

## O que aprendi

- Senhas fracas (como `admin123`) aparecem em listas de vazamentos e são as primeiras testadas
- Senha escrita no código é detectada pelo Bandit (B105)
- A correção é guardar só o **hash** da senha, fora do código, numa variável de ambiente
- Remover um segredo do código não basta: ele continua no histórico do Git

## Ferramentas

- SAST com Bandit
- SCA com pip-audit
- GitHub Actions
