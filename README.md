# Template de Segurança Python

Estrutura base para começar projetos Python com segurança desde o início.

## O que já vem pronto

- Pipeline no GitHub Actions
- SAST com Bandit
- SCA com pip-audit
- .gitignore protegendo senhas e arquivos locais

## Como usar

1. Clique em **Use this template**
2. Crie seu novo repositório
3. Troque o exemplo do `app.py` pelo código do seu projeto
4. Adicione as bibliotecas que você usar no `requirements.txt`
5. Atualize este README com o nome e a descrição do seu projeto
6. Faça um commit e veja a aba **Actions**

7. ## O que aprendi

- Senhas fracas (como `admin123`) aparecem em listas de vazamentos e são as primeiras testadas
- Senha escrita no código é detectada pelo Bandit (B105)
- A correção é guardar só o **hash** da senha, fora do código, numa variável de ambiente
- Remover um segredo do código não basta: ele continua no histórico do Git
