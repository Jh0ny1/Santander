
# Santander-Coders
Seguindo as Aulas da Iniciativa Santander Coders e replicando o que eu vejo nas aulas

## Ordem de Trabalho 

    1° Modificação ou alteração
    2° git add, modificação pronta para ser commitada
    3° git commit -m, para salvar o progresso
        + E começar tudo de novo, hahaha

## Comandos
    git init, faz a pasta virar um repositório

    git add, adiciona um arquivo ao repositório (já joga ele na área de staged)
        git add (nome do arquivo a ser adicionado)
    
    git diff, mostra as linhas adicionadas ou removidas enquanto não commitadas (após commitar as modificações usar git diff --stag)

    git commit -m "algum texto dizendo oq vc mudou", faz um save state das suas mudanças (Os commits não se sobre-escrevem)

    git config, mostra comandos
        git config --global, alterações em todo o compilador 
        git config --global user.name "name", seta um nome para se identificar, (identificação em trabalhos em grupo)
        git config --global user.email "email", seta um email para se identificar, (identificação em trabalhos em grupo)
        git config --global init.defaultBranch "tipo da branch", muda a branch de acordo com o nome nela
    
    git log, mostra o histórico de commits

    git restore, volta o código pro ultimo commit salva
        git resetore --staged "nome do arquivo", volta o código da area de staged para a area de modified

    git remote, "sei lá"
    




## Dicionário

   
- **Repositório**: Uma pasta que pode ser adicionada ao GitHub.

- **Commit**: Um "save state" das suas alterações, deve ser nomeado.

- **Branch**: Uma ramificação do código, permitindo o desenvolvimento paralelo.

- **Upstream**: Referência ao repositório remoto associado a seu repositório local.

- **Pull Request (PR)**: Pedido para incorporar alterações de uma branch para outra; comumente usado em colaborações.

- **Merge**: Combinação de alterações de uma branch em outra.

- **Conflict Resolution**: Processo de resolver conflitos durante um merge.

- **Branch Master**: Nome padrão da branch principal.

- **Branch Feature**: Ramificação usada para desenvolver novas funcionalidades.

- **Branch Release**: Ramificação usada para preparar uma versão para produção.

- **Clone**: Criar uma cópia local de um repositório remoto.

- **Git Ignore**: Arquivo que lista padrões de arquivos/diretórios que devem ser ignorados pelo Git.

- **Repository URL**: Endereço web ou caminho local que identifica um repositório.

- **Upstream Repository**: Repositório remoto original a partir do qual um fork é feito.

- **Downstream Repository**: Repositório que foi forked de um upstream repository.

- **Commit Hash**: Identificador único de um commit, geralmente um código alfanumérico.

- **Remote**: Um repositório conectado ao seu repositório local.

- **Origin**: Nome padrão do repositório remoto original.

- **Push**: Enviar alterações locais para um repositório remoto.

- **Pull**: Obter alterações de um repositório remoto.

- **Git Stash**: Temporariamente salva as mudanças que ainda não foram commitadas.

- **Cherry-pick**: Aplica um commit específico de uma branch para outra.

- **Rebase**: Reorganiza os commits para criar uma linha do tempo linear.

- **Tag**: Uma referência estática para um commit específico, geralmente usado para versões.

- **Git GUI**: Interface gráfica para o Git.

- **HEAD**: Referência ao commit mais recente na branch atual.

- **Detached HEAD**: Situação em que o HEAD não está em uma branch específica.

- **Pull with Rebase**: Combina o pull e o rebase em uma operação.

- **Squash**: Combina vários commits em um único commit.

- **Git Cherry**: Encontra commits que estão na branch atual mas não na outra.

- **Submodule**: Repositório Git incluído como um subdiretório em outro repositório Git.

- **Patch**: Arquivo que contém as diferenças entre dois commits.

- **Bare Repository**: Repositório sem uma cópia de trabalho.

- **Bisect**: Ajuda a encontrar o commit que introduziu um bug usando pesquisa binária.

- **Stash Pop**: Aplica as mudanças salvas no stash.

- **Pull Request Review**: Revisão de código realizada antes de aceitar um pull request.

- **Revert**: Desfaz um commit específico, criando um novo commit de reversão.

- **Reflog**: Registro de todas as referências ao HEAD, útil para recuperar estados anteriores.

- **Clean**: Remove arquivos não rastreados e alterações não commitadas.

- **Pre-commit Hook**: Script que é executado automaticamente antes de cada commit.

- **Post-commit Hook**: Script que é executado automaticamente após cada commit.

- **Pre-push Hook**: Script que é executado automaticamente antes de cada push.

- **GitHub Actions**: Automação de fluxos de trabalho no GitHub.

- **Gist**: Repositório Git pequeno, muitas vezes usado para compartilhar snippets de código.

- **Issue**: Rastreamento de tarefas, melhorias ou bugs no GitHub.

- **Continuous Integration (CI)**: Prática de integrar e testar código automaticamente.

- **Continuous Deployment (CD)**: Prática de implantar automaticamente código em produção após passar por CI.

- **Rebase Interactive**: Permite reorganizar commits de forma mais flexível.

- **Merge Conflict**: Ocorre quando há alterações conflitantes em um merge ou rebase.

- **Changelog**: Registro de todas as alterações feitas em um projeto.

- **Upstream Merge**: Atualização da branch atual com as alterações do upstream.

- **Repository Cloning**: Criar uma cópia local de um repositório remoto.

- **Rebase Abort**: Cancela um rebase em andamento.

- **Worktree**: Área de trabalho independente associada a um repositório.

- **Reset Hard**: Desfaz alterações no working directory e na área de staged.

- **Reset Soft**: Mantém alterações no working directory após desfazer a área de staged.

- **Contributing Guidelines**: Diretrizes para contribuir para um projeto, geralmente encontradas no arquivo CONTRIBUTING.md.

- **Hacktoberfest**: Evento anual para incentivar contribuições ao código aberto no GitHub durante outubro.


## Atalhos

    
- `Ctrl + L`: Limpa o terminal.
  
- `Ctrl + S`: Salva as alterações.

- `Ctrl + C`: Cancela a operação atual no terminal.

- `Tab`: Completa automaticamente nomes de arquivos e comandos.


## Etapas

- **Untracked**: Arquivos recentemente adicionados e não commitados, exibidos em vermelho.

- **Unmodified**: Mudanças realizadas, mas não movidas para a área de modified, também em vermelho.

- **Modified**: Alterações feitas, mas não salvas. Área intermediária entre unmodified e staged, útil para depuração.
  - Use `git add` para movê-las para a área de staged.

- **Staged**: Última etapa para modificações antes do commit, quando não há bugs.
  - Use `git commit -m "mensagem"` para salvar as alterações.   
