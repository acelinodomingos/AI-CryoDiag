# API de telemetria

A API FastAPI está em `src/api.py` e mantém um buffer local de leituras para desenvolvimento.

## Executar localmente

```bash
uvicorn src.api:app --reload
```

## Verificar saúde

```bash
curl http://127.0.0.1:8000/health
```

## Enviar telemetria

```bash
curl -X POST http://127.0.0.1:8000/telemetry \
  -H "Content-Type: application/json" \
  -d '{"tank_id":"TANK-001","pressure_bar":12.4,"level_percent":68.2,"temperature_c":-183.0}'
```

## Consultar leituras

```bash
curl "http://127.0.0.1:8000/telemetry?limit=20"
```

## MQTT

O cliente em `src/mqtt_client.py` publica uma leitura sintética. Configure `MQTT_HOST`, `MQTT_USERNAME` e `MQTT_PASSWORD` por variáveis de ambiente. Nunca coloque credenciais em arquivos versionados.

> Esta API é uma base de desenvolvimento. Para produção, adicione autenticação, persistência, TLS, observabilidade, limites de taxa e validação de segurança.

