
## Arquitetura do Sistema

```mermaid
graph TB
    subgraph "Tanques Criogênicos & Equipamentos Hospitalares"
        A[Sensores IoT<br/>Temperatura • Pressão • Nível • Vazão]
    end

    A -->|MQTT / LoRa| B[Edge Gateway<br/>Raspberry Pi / ESP32]

    B -->|TLS + MQTT| C[(Broker MQTT<br/>Mosquitto / EMQX)]

    C --> D[Ingestão de Dados<br/>Python + Paho-MQTT]
    D --> E[(Banco Timeseries<br/>PostgreSQL + TimescaleDB)]

    E --> F[Processamento IA/ML]
    subgraph "Motor de Inteligência Artificial"
        F1[Pré-processamento<br/>Scikit-learn]
        F2[Modelos TensorFlow/Keras<br/>• Detecção de anomalias<br/>• Previsão de falhas<br/>• Diagnóstico auxiliar]
        F3[Simulações criogênicas<br/>SymPy + NumPy]
        F1 --> F2
        F3 --> F2
    end

    F --> G[API Backend<br/>FastAPI / Flask]

    G --> H[Dashboard Web/Mobile<br/>React.js + Chart.js<br/>Alertas Push (Firebase)]

    G --> I[Integração com EMR<br/>HL7 / FHIR<br/>INCA • SIH/SUS]

    H & I --> J[Profissionais de Saúde<br/>Médicos • Enfermeiros<br/>Técnicos de Manutenção]

    style A fill:#1e40af, color:white
    style F fill:#7c3aed, color:white
    style H fill:#059669, color:white
    style J fill:#dc2626, color:white
