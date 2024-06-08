![](img/capaAda.png)
# Redes


## Modelo OSI / TCP-IP

![](img/OSI.png)

Acesso é de baixo pra cima
### MODELO OSI 
#### Mais próximo do usuário.
* **Aplicaçao**: Mais próxima do usuário, protocolos DNS, SSH
* **Apresentação**: Criptografia, conexão segura, pesistente. Responsável por criptografar os dados para a camada de sessão e também descriptografar os dados de volta para camada de Aplicação.
* **Sessão**: Responsável por estabelecer uma sessão entre origem e destino final. Como vai ser a forma de transmissão.

#### Mais a nível de hardware
* **Transporte**: Responsável também pela conexao com destino final através dos protocolos **TCP**, e **UDP**.
    
    * **TCP**:  Envia os dados para o destino final (segmento), garante a entrega. Ex(email,transações bancárias)
    * **UDP**: Envia os dados sem garantir a entrega. (Serviços de Streams de musica e vídeos).

* **Rede**: Recebe o segmento da camada de transporte e transforma em um pacote onde acontece o envio e recebimento de um roteador para outro.

* **Enlace**: Responsável por fragmentar os pacotes recebidos da camada de rede e transformá-los em quadros. Responsável por fazer a comunicação por endereços MAC.

* **Física**: Parte física da rede, cabos, switchs, placas, protocolos.

### MODELO TCP/IP
 Só muda a segmentação
* **Aplicação**: camadas de aplicação, apresentação e sessão do modelo OSI

* **Transporte**: Camada de transporte do modelo OSI.

* **Internet**: Camada de rede do modelo OSI.

* **Acesso a Rede**: Camadas de Enlace e Física do modelo OSI.

--------------------------------------------------------------
## IPv4 E IPv6

### IP - Internet Protocol
O termo IP (nternet Protocol) é o protocolo responsável pelo endereçamento dos pacotes de rede na camada 3 do modelo OSI, ou seja, é responsável por gerar um endereço ao seu computados, ou qualquer servidor, no momento que este conecta-se à internet. Atualmente existem dois formatos que são: **IPv4 e IPv6**.

**IPv4**: 192.168.0.1
--------------------------------------------------------------
Formato de 32 bits divididos em 8 octetos onde cada octeto pode variar de 0 até 255.
Criado na década de 80 e muito utilizado até hoje. Quando criado, a estimativa era que o IPv4 podesse receber até 4 bilhões de dispositivos, e esse limite chegou. Não tendo mais endereços ipv4 disponíveis. Para resolver esse problema foi criado o **NAT** (**Protocolo utilizado para permitir comunicação entre dispositivos com diferentes endereços IP**) que de forma mais simples, é responsável por converter Ips públicos emprivados e vice-versa.

**IPv6**: 1050:0000:0000:0000:0005:0600:300f:326b(11050:0:0:0:5:600:300c:326b)
-------------------------------------------------------------- 
Formato de 128 bits dividido em 16 pares. É a evolução do IPv4, em formato hexadecimal, sua utilização veio para resolver o problema da escasez de IPv4. Ainda não está muito presente no nosso dia-a-dia.

## CÁLCULO DE SUB-REDE
![Tabela de classes Ips](img/classeIp.png)