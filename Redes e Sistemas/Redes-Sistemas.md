# Infraestrutura de Redes e Principais Equipamentos

## Definição

A **infraestrutura de redes** engloba os componentes físicos e lógicos necessários para estabelecer a comunicação de dados entre dispositivos. Isso inclui a seleção adequada e a configuração de dispositivos essenciais.

## Equipamentos Principais

### 1. Roteadores

- Encaminham dados entre diferentes redes.

- Gerenciam tabelas de roteamento para determinar o melhor caminho.

### 2. Switches

- Facilitam a comunicação entre dispositivos na mesma rede.

- Operam na camada de Enlace do Modelo OSI.

### 3. Hubs

- Menos utilizados atualmente devido à sua simplicidade.

- Replicam dados para todos os dispositivos na rede, independentemente do destinatário.

### 4. Firewalls

- Monitoram e controlam o tráfego para proteger a rede contra ameaças.

- Estabelecem regras de segurança para permitir ou bloquear comunicações.

### 5. Servidores

- Oferecem serviços específicos, como armazenamento de arquivos, autenticação e hospedagem de sites.

- Podem ser dedicados a funções específicas, como servidores de e-mail ou DNS.

# Termos mais usados

## Topologia de Rede

**Topologia de Rede**:
Arranjo físico ou lógico dos dispositivos em uma rede.
Exemplos: topologia em estrela, topologia em anel.

**Gateway**:
Ponto de entrada ou saída entre duas redes.
Roteadores frequentemente atuam como gateways.

**Rede LAN/WAN**:
- **LAN (Local Area Network)**: Refere-se a uma rede local.
- **WAN (Wide Area Network)**: É uma rede que cobre uma área geográfica maior.

**DHCP (Dynamic Host Configuration Protocol)**:
Protocolo que atribui dinamicamente endereços IP a dispositivos em uma rede.

## Cabeamento Estruturado

### Definição

O **cabeamento estruturado** é um sistema padronizado de cabos e conectores que facilita a administração e manutenção da infraestrutura de redes. Isso permite uma fácil adaptação às mudanças na rede.

### Importância

- **Flexibilidade**: Permite adicionar, remover ou mover dispositivos sem redesenhar a infraestrutura. Facilita a organização e a manutenção.

- **Desempenho**: Influencia na velocidade e confiabilidade da comunicação de dados. Reduz interferências e perdas de sinal.

# Termos mais usados

**Patch Panel**:
Painel que centraliza conexões de cabos, facilitando a manutenção.

**Keystone Jack**:
Conector que se encaixa em uma tomada de parede ou painel.

**Fibra Óptica**:
Meio de transmissão que utiliza luz para transmitir dados.
Oferece alta largura de banda e baixa perda de sinal.

**Crossover Cable**:
Cabo que conecta dispositivos sem a necessidade de um switch.

## Modelo OSI e TCP/IP

### Modelo OSI

- **Camada Física**: Lida com a transmissão e recepção de bits pela rede.

- **Camada de Enlace**: Gerencia o acesso ao meio físico e o controle de erros.

- **Camada de Rede**: Roteamento de pacotes e determinação de rotas.

- **Camada de Transporte**: Controle de fluxo e correção de erros.

- **Camada de Sessão**: Estabelecimento, manutenção e encerramento de sessões.

- **Camada de Apresentação**: Tradução de formatos de dados.

- **Camada de Aplicação**: Fornece interfaces para os serviços de rede.

### TCP/IP

- **Camada de Enlace**: Equivalente à camada de Enlace do OSI. Lida com a transmissão de quadros.

- **Camada de Rede**: Combina funcionalidades da camada de Rede e Transporte do OSI. Gerencia o endereçamento IP.

- **Camada de Transporte**: Responsável pelo controle de fluxo e correção de erros.

- **Camada de Aplicação**: Engloba funções das camadas de Sessão, Apresentação e Aplicação do OSI.


# Termos mais usados

**Packet/Switching**:
Técnica em que dados são divididos em pacotes para transmissão eficiente.

**Protocolo**:
Conjunto de regras que define como os dados são transmitidos na rede.

**TCP (Transmission Control Protocol)**:
Protocolo de transporte confiável usado no modelo TCP/IP.

**UDP (User Datagram Protocol)**:
Protocolo de transporte mais rápido, mas menos confiável que o TCP.

## IPV4 e IPV6

### IPV4

**Sistema de Endereçamento**:

- Utiliza endereços de 32 bits, resultando em cerca de 4,3 bilhões de combinações possíveis.

- Limitações devido à crescente demanda por endereços IP.

### IPV6

**Sistema de Endereçamento**:

- Utiliza endereços de 128 bits, proporcionando um vasto número de combinações.

- Desenvolvido para superar a escassez de endereços do IPV4.

# Termos mais usados

**Endereço IP**:
Identificador numérico atribuído a cada dispositivo em uma rede.

**Máscara de Sub-rede**:
Determina a quantidade de bits usados para identificar a sub-rede.

**Gateway Padrão**:
Roteador usado para encaminhar dados fora da rede local.

**Broadcast**:
Transmissão de dados para todos os dispositivos em uma rede.

## Cálculo de Sub-rede

### Definição

O **cálculo de sub-rede** envolve dividir uma rede IP em sub-redes menores para otimizar o uso de endereços IP. Isso é essencial para o gerenciamento eficiente de redes.

### Ferramentas e Fórmulas

- **Calculadoras de Sub-rede**: Facilitam o processo, fornecendo resultados precisos.

- **Fórmulas**: Determinam o número de sub-redes e hosts por sub-rede com base nos requisitos.

# Termos mais usados

**CIDR (Classless Inter-Domain Routing)**:
Notação que representa um bloco de endereços IP e sua máscara de sub-rede.

**Hosts por Sub-rede**:
Número de dispositivos que podem ser conectados a uma sub-rede.

**Roteamento Estático**:
Configuração manual de rotas em um roteador.


## Domínios, DNS e Latência

### Domínios

**Definição**:

- Representam espaços organizacionais na internet.

- Exemplos incluem domínios de alto nível (.com, .org) e domínios de país (.br, .us).

### DNS (Domain Name System)

**Função**:

- Traduz nomes de domínio em endereços IP.

- Facilita a navegação na web usando nomes amigáveis.

### Latência

**Definição**:

- Tempo de atraso na comunicação de dados.

- Influencia diretamente na eficiência e velocidade da rede.


# Termos mais usados

**Nome de Domínio**:
Identificador alfanumérico associado a um endereço IP.

**Registro DNS**:
Entrada em um servidor DNS associando um nome de domínio a um endereço IP.

**Ping Time**:
Tempo necessário para um pacote viajar de um ponto a outro na rede.

## Principais Comandos de Configuração

**Comandos Fundamentais**:

- `ipconfig`: Exibe configurações de IP e outros parâmetros de rede no Windows.

- `ping`: Testa a conectividade entre dois dispositivos.

- `tracert`: Rastreia a rota que os pacotes seguem até o destino.

- `netstat`: Mostra as conexões de rede ativas.

**Utilidade**:

Esses comandos são cruciais para diagnosticar, configurar e verificar a conectividade e o status da rede.

## Segurança

### Firewalls e Antivírus

**Firewalls**:

- Monitoram e controlam o tráfego de rede, bloqueando ameaças.

- Podem ser baseados em hardware ou software.

**Antivírus**:

- Detectam e removem software malicioso.

- Essenciais para proteger sistemas contra ataques.

### Políticas de Segurança

**Definição**:

- Estabelecem regras sobre quem pode acessar quais recursos e quando.

- Garantem a integridade, confidencialidade e disponibilidade dos dados.


# Termos mais usados


**VPN (Virtual Private Network)**:
Rede privada virtual que utiliza a internet para conectar usuários remotamente.

**Intrusion Detection System (IDS)**:
Sistema que monitora atividades na rede para identificar possíveis ameaças.

**PKI (Public Key Infrastructure)**:
Infraestrutura que gerencia chaves criptográficas para garantir segurança.

## Wireless

### Redes Sem Fio

- **Wi-Fi**: Permite a comunicação sem fio entre dispositivos. Amplamente utilizado para proporcionar mobilidade.

### Padrões

- **WPA/WPA2**: Protocolo de segurança crucial para proteger redes Wi-Fi. Criptografa dados para evitar acesso não autorizado.

# Termos mais usados

**SSID (Service Set Identifier)**:
Nome da rede Wi-Fi.

**WEP/WPA/WPA2**:
Protocolos de segurança para redes Wi-Fi, com WPA2 sendo o mais seguro.

**Channel**:
Frequência específica em que a rede sem fio opera.