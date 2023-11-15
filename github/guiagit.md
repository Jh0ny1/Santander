# SantanderCoders 
Seguindo as Aulas da Iniciativa Santander Coders e replicando o que eu vejo nas aulas

# Git & GitHub

## Ordem de Trabalho 

1. Modificação ou Alteração

2. ```git add <nome_do_arquivo>```: Prepara a modificação para ser commitada.

3. ```git commit -m "mensagem"```: Salve o progresso com uma mensagem descritiva.

4. ```git push origin "branch que vc ta usando"```. (Se não der certo use ```git remote -v```, se não aparecer nada é pq vc não linkou com o repositorio remoto use ```git remote add origin "URL do repositorio"```).

5. Volte ao ínicio do processo.


## Comandos

 ```git init```: Transforma a pasta em um repositório Git.

 ```git add <nome_do_arquivo>```: Adiciona um arquivo ao repositório (colocao na área de staged).
  
 ```git diff```: Mostra as linhas adicionadas ou removidas ainda não commitadas (após commitar, use git diff staged).

 ```git commit m "mensagem"```: Salva um estado das mudanças (os commits não se sobrescrevem).
  
 ```git config```: Mostra comandos de configuração. 

 ```git config global```: Altera configurações globalmente.  

 ```git config global user.name "nome"```: Define um nome de usuário (útil para trabalhos em grupo).  
 
 ```git config global user.email "email"```: Define um email para identificação.  

 ```git config global init.defaultBranch "nome_da_branch"```: Muda a branch padrão.


 ```git log```: Exibe o histórico de commits.

 ```git restore```: Volta o código para o último commit salvo.

 ```git restore staged <nome_do_arquivo>```: Volta o arquivo da área de staged para a área de modified.

 ```git remote```: Conecta seu repositório local a um repositório remoto.

 ```git remote add origin <url>```: Adiciona um repositório remoto chamado "origin".
 
 ```git push```: Envia seus commits para um repositório remoto.  
 
 ```git push u origin <nome_da_branch>```: Define a branch remota como upstream.

 ```git pull```: Obtém alterações de um repositório remoto.

 ```git pull origin <nome_da_branch>```: Obtém as alterações da branch remota.

 ```git fetch```: Obtém todas as branches e tags de um repositório remoto, sem mesclálas com a sua versão local.

 ```git merge```: Combina alterações de uma branch para outra.
   ```git merge <nome_da_branch>```: Realiza o merge da branch especificada na branch atual.

 ```git checkout```: Altera a branch atual ou restaura arquivos.
   ```git checkout b <nome_da_branch>```: Cria e muda para uma nova branch.
   ```git checkout <nome_da_branch>```: Muda para uma branch existente.

 ```git branch```: Lista, cria ou deleta branches.
   ```git branch d <nome_da_branch>```: Deleta uma branch local.

 ```git tag```: Lista, cria ou deleta tags.
   ```git tag a <nome_da_tag> m "mensagem"```: Cria uma tag anotada.

 ```git log```: Exibe o histórico de commits.
   ```git log oneline```: Exibe o histórico de commits em uma única linha.

 ```git blame```: Mostra quem modificou cada linha de um arquivo e em qual commit.

 ```git revert```: Desfaz um commit específico, criando um novo commit de reversão.

 ```git cherrypick```: Aplica um commit específico de uma branch para outra.

 ```git submodule```: Adiciona submódulos a um repositório.

 ```git stash```: Salva temporariamente as mudanças que ainda não foram commitadas.

 ```git grep```: Procura por um padrão em seus arquivos do repositório.

 ```git log --oneline --decorate```: Mostra a branch, e os codigos dos commits.


## Atalhos

 + Ctrl + L: Limpa o terminal.
  
 - Ctrl + S: Salva as alterações.

 + Ctrl + C: Cancela a operação atual no terminal.

 + Tab: Completa automaticamente nomes de arquivos e comandos.

 + Ctrl + X: Corta o texto selecionado.

 + Ctrl + V: Cola o texto copiado.

 + Ctrl + Z: Desfaz a última ação.

 + Ctrl + Y: Refaz a última ação desfeita.


## Dicionário

* **Fork:** Criar uma cópia independente de um repositório, permitindo o desenvolvimento separado.

* **Repositório:** Uma pasta que pode ser adicionada ao GitHub.

* **Commit:** Um "save state" das suas alterações, deve ser nomeado.

* **Branch:** Uma ramificação do código, permitindo o desenvolvimento paralelo.

* **Upstream:** Referência ao repositório remoto associado a seu repositório local.

* **Pull Request (PR):** Pedido para incorporar alterações de uma branch para outra; comumente usado em colaborações.

* **Merge:** Combinação de alterações de uma branch em outra.

* **Conflict Resolution:** Processo de resolver conflitos durante um merge.

* **Branch Master:** Nome padrão da branch principal.

* **Branch Feature:** Ramificação usada para desenvolver novas funcionalidades.

* **Branch Release:** Ramificação usada para preparar uma versão para produção.

* **Clone:** Criar uma cópia local de um repositório remoto.

* **Git Ignore:** Arquivo que lista padrões de arquivos/diretórios que devem ser ignorados pelo Git.

* **Repository URL:** Endereço web ou caminho local que identifica um repositório.

* **Upstream Repository:** Repositório remoto original a partir do qual um fork é feito.

* **Downstream Repository:** Repositório que foi forked de um upstream repository.

* **Commit Hash:** Identificador único de um commit, geralmente um código alfanumérico.

* **Remote:** Um repositório conectado ao seu repositório local.

* **Origin:** Nome padrão do repositório remoto original.

* **Push:** Enviar alterações locais para um repositório remoto.

* **Pull:** Obter alterações de um repositório remoto.

* **Git Stash:** Temporariamente salva as mudanças que ainda não foram commitadas.

* **Cherrypick:** Aplica um commit específico de uma branch para outra.

* **Rebase:** Reorganiza os commits para criar uma linha do tempo linear.

* **Tag:** Uma referência estática para um commit específico, geralmente usado para versões.

* **Git GUI:** Interface gráfica para o Git.

* **HEAD:** Referência ao commit mais recente na branch atual.

* **Detached HEAD:** Situação em que o HEAD não está em uma branch específica.

* **Pull with Rebase:** Combina o pull e o rebase em uma operação.

* **Squash:** Combina vários commits em um único commit.

* **Git Cherry:** Encontra commits que estão na branch atual mas não na outra.

* **Submodule:** Repositório Git incluído como um subdiretório em outro repositório Git.

* **Patch:** Arquivo que contém as diferenças entre dois commits.

* **Bare Repository:** Repositório sem uma cópia de trabalho.

* **Bisect:** Ajuda a encontrar o commit que introduziu um bug usando pesquisa binária.

* **Stash Pop:** Aplica as mudanças salvas no stash.

* **Pull Request Review:** Revisão de código realizada antes de aceitar um pull request.

* **Revert:** Desfaz um commit específico, criando um novo commit de reversão.

* **Reflog:** Registro de todas as referências ao HEAD, útil para recuperar estados anteriores.

* **Clean:** Remove arquivos não rastreados e alterações não commitadas.

* **Precommit Hook:** Script que é executado automaticamente antes de cada commit.

* **Postcommit Hook:** Script que é executado automaticamente após cada commit.

* **Prepush Hook:** Script que é executado automaticamente antes de cada push.

* **GitHub Actions:** Automação de fluxos de trabalho no GitHub.

* **Gist:** Repositório Git pequeno, muitas vezes usado para compartilhar snippets de código.

* **Issue:** Rastreamento de tarefas, melhorias ou bugs no GitHub.

* **Continuous Integration (CI):** Prática de integrar e testar código automaticamente.

* **Continuous Deployment (CD):** Prática de implantar automaticamente código em produção após passar por CI.

* **Rebase Interactive:** Permite reorganizar commits de forma mais flexível.

* **Merge Conflict:** Ocorre quando há alterações conflitantes em um merge ou rebase.

* **Changelog:** Registro de todas as alterações feitas em um projeto.

* **Upstream Merge:** Atualização da branch atual com as alterações do upstream.

* **Repository Cloning:** Criar uma cópia local de um repositório remoto.

* **Rebase Abort:** Cancela um rebase em andamento.

* **Worktree:** Área de trabalho independente associada a um repositório.

* **Reset Hard:** Desfaz alterações no working directory e na área de staged.

* **Reset Soft:** Mantém alterações no working directory após desfazer a área de staged.

* **Contributing Guidelines:** Diretrizes para contribuir para um projeto, geralmente encontradas no arquivo CONTRIBUTING.md.

* **Hacktoberfest:** Evento anual para incentivar contribuições ao código aberto no GitHub durante outubro.


## Etapas

 **Untracked:** Arquivos recentemente adicionados e não commitados, exibidos em vermelho.

 **Unmodified:** Mudanças realizadas, mas não movidas para a área de modified, também em vermelho.

 **Modified:** Alterações feitas, mas não salvas. Área intermediária entre unmodified e staged, útil para depuração.
   Use ```git add``` para movêlas para a área de staged.

 **Staged:** Última etapa para modificações antes do commit, quando não há bugs.
   Use ```git commit m "mensagem"``` para salvar as alterações.   
