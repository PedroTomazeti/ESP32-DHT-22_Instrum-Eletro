# ESP32-DHT-22_Instrum-Eletro
Projeto do Sensor DHT22 utilizando ESP32 com MQTT<br>
Este projeto foi desenvolvido como parte da disciplina de Instrumentação Eletrônica da Universidade Estadual do Maranhão (UEMA). Ele utiliza do micropy no ESP32 de e se comunica via Broker MQTT mosquitto.

Descrição do Projeto<br>
O objetivo deste projeto é medir a temperatura e umidade utilizando um sensor DHT22, e publicar essas medições em um broker MQTT. Acessar esses dados via código para o cálculo da incerteza. A comunicação é realizada através de uma conexão Wi-Fi.

Integrantes da Equipe <br>
João Marcos Vidal Lacerda <br>
Luiz Felipe Freitas Ferreira <br>
Lucas de Menezes Pereira <br>
Pedro Lucas Tomazeti Fernandes <br>
Rebeca Cristina Sousa Vieira de Carvalho

Componentes Utilizados
```
Sensor DHT22: Sensor de temperatura e umidade.
MQTT Broker: Utilizado para comunicação MQTT. O broker utilizado neste projeto é o test.mosquitto.org.
Resistores e Jumpers.
Wi-Fi: Conexão com a rede local.
```
Configurações do MQTT
```
MQTT_CLIENT_ID: "pedro-tomazeti-micropy"
MQTT_BROKER: "test.mosquitto.org"
MQTT_USER: ""
MQTT_PASSWORD: ""
MQTT_TOPIC: "instrum-eletro"
```
Funcionamento
```
Inicialização do Sensor DHT22: O sensor é inicializado no pino 18.
Conexão Wi-Fi: O dispositivo se conecta à rede Wi-Fi do Local.
Conexão ao Broker MQTT: Uma conexão é estabelecida com o broker MQTT test.mosquitto.org.
Medição e Publicação: O código mede a temperatura e a umidade utilizando o sensor DHT22, e publica essas medições no tópico MQTT instrum-eletro a cada 2 segundos, caso haja uma nova medição.
Leitura dos dados: Os outros códigos são para receber as informações do tópico em tempo real, salvá-los em .CSV e logo após fazer o cálculo da média, desvio padrão e o grau de incerteza tipo 2.
```
Método de Teste <br>
Este código é projetado para ser executado no ESP32 com micropython.

Disciplina <br>
Este projeto foi desenvolvido para a disciplina de Instrumentação Eletrônica da Universidade Estadual do Maranhão (UEMA).
