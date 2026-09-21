# AI-CryoDiag
   🚀 **[CLIQUE AQUI PARA VER O DASHBOARD AO VIVO](https://ai-cryodiag-gohujcmxnmxddww3v7vtkl.streamlit.app/)**
**Sistema de Inteligência Artificial para diagnóstico e monitoramento de armazenamento criogênico de fármacos gasosos no SUS**

[![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)](https://github.com/acelinodomingos/AI-CryoDiag)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Autor](https://img.shields.io/badge/Autor-Acelino%20Domingos%20Correia%20Filho-blue)](https://github.com/acelinodomingos)

---

## Motivação

Hospitais e institutos de saúde que armazenam fármacos gasosos (oxigênio e nitrogênio líquido) em tanques criogênicos de alta capacidade enfrentam um desafio constante: monitorar nível e pressão em tempo real para evitar riscos de segurança e desperdício, além de otimizar a logística de reposição.

Este projeto nasceu da experiência prática de gestão da rede de criogênicos e fármacos gasosos do **Instituto Nacional de Câncer (INCA/RJ)**, onde um sistema de sensores e alarmes de nível crítico foi parcialmente implementado entre 2015 e 2019.

O **AI-CryoDiag** retoma essa base e propõe uma camada de **Inteligência Artificial** sobre a telemetria — indo do simples alarme para o **diagnóstico preditivo**.

---

## O que o projeto propõe

- Monitoramento de nível, pressão e temperatura em tempo real
- Detecção antecipada de riscos (vazamento, queda crítica de nível, falha de isolamento)
- Machine Learning para prever necessidade de reposição
- Redução de custos logísticos e aumento da segurança
- Foco prioritário em unidades de saúde pública (SUS)

---

## Arquitetura do Sistema

```mermaid
graph TB
    A["Tanques Criogênicos<br/>Oxigênio e Nitrogênio Líquido"]
    B["Sensores de Pressão<br/>(0-25 bar)"]
    C["Sensores de Nível<br/>(Ultrasônico / Radar)"]
    D["Sensores de Temperatura<br/>(PT100 / Termopar)"]
    E["Gateways IoT<br/>(ESP32 / Raspberry Pi)"]
    F["Brokers MQTT<br/>(Mosquitto / EMQX)"]
    G["Alertas Push"]
    H["Dashboards Web"]
    I["Modelos de Machine Learning"]
    J["Bancos de Dados<br/>(InfluxDB + PostgreSQL)"]
    K["APIs REST<br/>(FastAPI)"]
    L["Apps Mobile"]

    A --> B & C & D
    B & C & D --> E
    E -->|Telemetria| F
    F --> G & H & I & J
    J --> K
    K --> H & L
