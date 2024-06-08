![](img/capaAda.png)
# Git / GitHub - Versionamento de Código

* Versionamento: inclusão do registro de mudanças em arquivos que possibilita a recuperação ou acesso a versões anteriores.

* Git: Software de versionamento de código que guarda **snapshots** do estado  de projetos e arquivos, além de uma referência/caminho para este snapshot.

As maiorias das alterações feitas pelo Git são locais e por isso, boa parte as operações são praticamente instantâneas devido à facillidade de acessar arquivos em seu próprio computador.

## Configuração inicial

```bash
$ git config --global user.name"nomeDoUsuário" # Registra o usuário do repositório
$ git config --global user.email seu@email.com # Registra o email do usuário do repositório
```

## Manipulação de repositórios

### Clonar um repositório existente a partir de um link no GitHub
```bash
# git clone <link do repositório>
$ git clone https://github.com/code50/111503993.git
```
Ficar atento as opções de link para clonar um repositório.

### Iniciar um repositório Vazio localmente
```bash
$ git init
```

### Verificar se um repositório local está linkado a algum repositório remoto

```bash
$ git remote -v
```

### Conectar um repositório local a um remoto

```bash
# git remote add origin <link do repositório>
$ git remote add origin https://github.com/code50/111503993.git
```

### Clonar uma branch de um repositório
```bash
# git clone <URLdoRepositorio> --branch <nomeDaBrabch> --single-branch

$ git clone git@github.com:JhonCostaDev/estudoGit-citacoes.git --branch ada --single-branch 
```

## Gravando mudanças no repositório local

### Classificação do estado de um arquivo no Git

* **Untraked**: Não rastreado, quando você cria um novo arquivo ou adiciona um arquivo ao diretório, o Git o consiera "não rastreado".
* **Unmodified**:
* **Modified**: Modificado, quando você faz alterações em um arquivo que já está sendo rastreado.
* **Staged**: Preparado, após modificar um arquivo, podemos prepará-lo para o próximo commit usando o comando git add.

### Exibi status do repositório
```bash
$ git status
```

### Adicionando arquivos na área de preparação

```bash
# git add <nome do arquivo>
$ git add README.md
# git add . adiciona todas as modificações
$ git add .

```



