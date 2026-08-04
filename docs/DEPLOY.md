# Execução e publicação

## API com Docker

Na raiz do repositório:

```bash
docker build -t ai-cryodiag-api .
docker run --rm -p 8000:8000 ai-cryodiag-api
```

Acesse a documentação interativa em `http://localhost:8000/docs`.

## Dashboard

Abra `dashboard/index.html` em um navegador ou publique o diretório como página estática. O dashboard atual usa dados sintéticos e é uma interface demonstrativa.

## MQTT com segurança

Defina as variáveis antes de executar o publicador:

```bash
export MQTT_HOST=broker.exemplo.local
export MQTT_USERNAME=usuario
export MQTT_PASSWORD='senha-fora-do-repositorio'
python src/mqtt_client.py
```

Em ambiente real, use TLS, ACLs, rotação de credenciais e rede segregada. O projeto não deve ser ligado a equipamentos hospitalares sem validação técnica, segurança cibernética e aprovação institucional.

