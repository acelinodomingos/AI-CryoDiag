## Arquitetura do Sistema

```mermaid
graph TB
    A["Tanques Criogênicos<br/>Oxigênio e Nitrogênio Líquido"]
    B["Sensores de Pressão<br/>(0-25 bar)"]
    C["Sensores de Nível<br/>(Ultrasônico / Radar)"]
    D["Sensores de Temperatura<br/>(PT100 / Termopar)"]
    E["Gateways IoT<br/>(ESP32 / Raspberry Pi)"]
    F["Brokers MQTT<br/>(Mosquitto / EMQX / HiveMQ)"]
    G["Alertas Push<br/>(Firebase Cloud Messaging)"]
    H["Dashboards Web<br/>(React.js + Chart.js)"]
    I["Modelos de Machine Learning<br/>(Detecção de vazamentos e falhas)"]
    J["Bancos de Dados<br/>(InfluxDB + PostgreSQL)"]
    K["APIs REST<br/>(FastAPI / Flask)"]
    L["Apps Mobile<br/>(Flutter / React Native)"]

    A --> B & C & D
    B & C & D --> E
    E -->|Telemetria em tempo real| F
    F --> G & H & I & J
    J --> K
    K --> H & L
    H & L -->|Notificações críticas| G

    classDef hardware fill:#1f6feb,stroke:#fff,color:#fff
    classDef cloud fill:#ff5722,stroke:#fff,color:#fff
    classDef frontend fill:#4caf50,stroke:#fff,color:#fff
    classDef ml fill:#9c27b0,stroke:#fff,color:#fff

    class A,B,C,D,E hardware
    class F,G,J cloud
    class H,L frontend
    class I ml
