## Diagrama de Arquitetura do AI-CryoDiag

```mermaid# AI-CryoDiag  
**Sistema de Inteligência Artificial para Monitoramento e Diagnóstico Predictivo de Tanques Criogênicos no SUS**

Monitoramento em tempo real de **centenas/milhares** de tanques de oxigênio líquido e nitrogênio em hospitais, UPAs e centrais de abastecimento do SUS, com detecção precoce de vazamentos, falhas e desperdício de gases medicinais.

## Arquitetura do Sistema

```mermaid
graph TB
    A["Tanques Criogênicos<br/>(Oxigênio Líquido / Nitrogênio Líquido)"]
    B["Sensores de Pressão<br/>(0-25 bar)"]
    C["Sensores de Nível<br/>(Ultrasônico / Radar)"]
    D["Sensores de Temperatura<br/>(PT100 / Termopar)"]
    E["Gateways IoT<br/>(ESP32 / Raspberry Pi 4)"]
    F["Brokers MQTT<br/>(Mosquitto / EMQX / HiveMQ)"]
    G["Alertas Push em Tempo Real<br/>(Firebase Cloud Messaging)"]
    H["Dashboards Web<br/>(React.js + Chart.js + Tailwind)"]
    I["Modelos de Machine Learning<br/>(Detecção de vazamentos e falhas)"]
    J["Bancos de Dados<br/>(InfluxDB + PostgreSQL)"]
    K["APIs REST<br/>(FastAPI / Flask)"]
    L["Aplicativos Mobile<br/>(Flutter ou React Native)"]

    A --> B
    A --> C
    A --> D
    B & C & D --> E
    E -->|Telemetria em tempo real| F
    F --> G
    F --> H
    F --> I
    F --> J
    J --> K
    K --> H
    K --> L
    H & L -->|Notificações críticas| G

    classDef hardware fill:#1f6feb,stroke:#fff,color:#fff
    classDef cloud fill:#ff5722,stroke:#fff,color:#fff
    classDef frontend fill:#4caf50,stroke:#fff,color:#fff
    classDef ml fill:#9c27b0,stroke:#fff,color:#fff

    class A,B,C,D,E hardware
    class F,G,J cloud
    class H,L frontend
    class I ml
graph TB
    A["Tanque Criogênico<br/>Oxigênio Líquido / Nitrogênio Líquido"]
    B["Sensor de Pressão<br/>(0-25 bar)"]
    C["Sensor de Nível<br/>(Ultrasônico / Radar)"]
    D["Sensor de Temperatura<br/>(PT100 / Termopar)"]
    E["Gateway IoT<br/>(ESP32 / Raspberry Pi 4)"]
    F["MQTT Broker<br/>(Mosquitto / EMQX / HiveMQ)"]
    G["Alertas Push em Tempo Real<br/>(Firebase Cloud Messaging)"]
    H["Dashboard Web<br/>(React.js + Chart.js + Tailwind)"]
    I["Modelo de Machine Learning<br/>(Detecção de vazamentos e falhas)"]
    J["Banco de Dados<br/>(InfluxDB + PostgreSQL)"]
    K["API REST<br/>(FastAPI / Flask)"]
    L["App Mobile<br/>(Flutter ou React Native)"]

    A --> B
    A --> C
    A --> D
    B & C & D --> E
    E -->|Telemetria em tempo real| F
    F --> G
    F --> H
    F --> I
    F --> J
    J --> K
    K --> H
    K --> L
    H & L -->|Notificações críticas| G

    classDef hardware fill:#1f6feb,stroke:#fff,color:#fff
    classDef cloud fill:#ff5722,stroke:#fff,color:#fff
    classDef frontend fill:#4caf50,stroke:#fff,color:#fff
    classDef ml fill:#9c27b0,stroke:#fff,color:#fff

    class A,B,C,D,E hardware
    class F,G,J cloud
    class H,L frontend
    class I ml
