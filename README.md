## Diagrama de Arquitetura do Sistema

```mermaid
graph TB
    A[Tanque Criogênico<br/>Oxigênio Líquido / Nitrogênio Líquido]
    B[Sensor de Pressão<br/>(0-25 bar)]
    C[Sensor de Nível<br/>(Ultrasônico / Radar)]
    D[Sensor de Temperatura<br/>(PT100 / Termopar)]
    E[Gateway IoT<br/>(ESP32 / Raspberry Pi 4)]
    F[MQTT Broker<br/>(Mosquitto / EMQX / HiveMQ)]
    G["Alertas Push em Tempo Real<br/>(Firebase Cloud Messaging)"]
    H["Dashboard Web<br/>(React.js + Chart.js + Tailwind)"]
    I["Modelo de Machine Learning<br/>(Detecção de vazamentos e falhas)"]
    J[Banco de Dados<br/>(InfluxDB + PostgreSQL)]
    K[API REST<br/>(FastAPI / Flask)]
    L[App Mobile<br/>(Flutter ou React Native)]

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

    classDef hardware fill:#1f6feb,stroke:#333,color:#fff
    classDef cloud fill:#ff5722,stroke:#333,color:#fff
    classDef frontend fill:#4caf50,stroke:#333,color:#fff
    classDef ml fill:#9c27b0,stroke:#333,color:#fff

    class A,B,C,D,E hardware
    class F,G,J cloud
    class H,L frontend
    class I ml
