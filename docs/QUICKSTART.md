# Início rápido

## Executar o simulador

O simulador usa Python 3.10+ e gera apenas dados sintéticos.

```bash
python src/telemetry_simulator.py --tank-id TANK-001 --count 5 --interval 1
```

Cada linha produz um evento JSON com pressão, nível, temperatura, horário UTC e indicação de anomalia.

## Testar anomalias

```bash
python src/telemetry_simulator.py --count 20 --anomaly-rate 0.20
```

O parâmetro `--anomaly-rate` deve ficar entre `0` e `1`.

## Executar testes

Com pytest instalado:

```bash
pytest -q
```

## Segurança

Os dados são sintéticos. Não conecte este exemplo diretamente a um tanque, controlador ou rede hospitalar. Qualquer uso operacional exige validação, calibração, revisão de segurança e profissionais habilitados.

