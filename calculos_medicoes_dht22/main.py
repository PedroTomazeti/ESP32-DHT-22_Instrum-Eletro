#CÓDIGO ESP32

import network       # Importa o módulo para configurar e gerenciar conexões de rede
import time          # Importa o módulo para funções relacionadas ao tempo (pausas, contagem, etc.)
from machine import Pin # Importa o módulo para controle dos pinos GPIO
import dht           # Importa o módulo para sensores DHT
import ujson         # Importa o módulo para manipulação de JSON
from umqtt.simple import MQTTClient  # Importa o módulo para comunicação MQTT

# Parametros do MQTT Server
MQTT_CLIENT_ID = "instrum-eletro-micropy"  # Identificador do cliente MQTT
MQTT_BROKER    = "test.mosquitto.org"  # Endereço do broker MQTT
MQTT_USER      = ""   # Usuário MQTT (vazio, sem autenticação)
MQTT_PASSWORD  = ""   # Senha MQTT (vazio, sem autenticação)
MQTT_TOPIC     = "instrum-eletro"  # Tópico MQTT para publicação


# Configuração do pino do DHT22
dht_pin = Pin(18)  # Use o pino GPIO onde o DHT22 está conectado
sensor = dht.DHT22(dht_pin)

# Conexão WIFI
print("Conectando ao Wifi", end="")
sta_if = network.WLAN(network.STA_IF)  # Cria uma interface de rede no modo estação
sta_if.active(True)  # Ativa a interface de rede
sta_if.connect("sua rede", "sua senha")  # Conecta à rede WiFi com SSID da sua rede e senha
while not sta_if.isconnected():
  print(".", end="")
  time.sleep(0.1)  # Espera até a conexão ser estabelecida
print(" Conectado!")

# Conexão ao servidor MQTT
print("Conectando ao MQTT server... ", end="")
client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, user=MQTT_USER, password=MQTT_PASSWORD)  # Cria um cliente MQTT
conectado = False
try:
  client.connect()  # Tenta conectar ao broker MQTT
  conectado = True
  print("Conectado!")
except Exception as e:
  print(f"Failed to connect to MQTT broker: {e}")  # Lida com falhas de conexão
  # Handle the exception or retry connection

if conectado:
  clima_anterior = ""  # Armazena a última medição de clima
  while True:
    print("Mensurando condições climáticas...", end="")
    sensor.measure()  # Mede temperatura e umidade
    message = ujson.dumps({
      "temp": sensor.temperature(),  # Obtém a temperatura medida
      "umidade": sensor.humidity(),   # Obtém a umidade medida
    })
    if message != clima_anterior:
      print(" Nova medição encontrada!")
      print(f"Enviando atualização ao MQTT topic {MQTT_TOPIC}: {message}")
      client.publish(MQTT_TOPIC,  message)  # Publica a nova medição no tópico MQTT
      clima_anterior = message  # Atualiza a última medição
    else:
      print(" Nenhuma atualização.")
    time.sleep(2)  # Espera 2 segundo antes de medir novamente
else:
  print("Não foi possível estabelecer conexão ao MQTT. Tente novamente.")  # Mensagem de erro se a conexão MQTT falhar
