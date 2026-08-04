# AI-CryoDiag — Documento de projeto

## Objetivo

Desenvolver uma base de monitoramento inteligente para tanques criogênicos de gases medicinais, com foco em continuidade operacional, rastreabilidade e apoio à manutenção hospitalar.

## Escopo inicial

O protótipo deve coletar pressão, nível e temperatura, registrar as leituras com data e hora, identificar desvios do comportamento esperado e apresentar alertas compreensíveis para a equipe responsável.

## Princípios

- Segurança em primeiro lugar;
- Nenhum alerta de software substitui inspeção, instrumento certificado ou protocolo técnico;
- Dados devem ser anonimizados quando usados para pesquisa;
- Toda decisão crítica deve ter revisão humana;
- O sistema deve ser auditável, documentado e adequado a ambientes com conectividade limitada.

## Fluxo de referência

1. Sensores fazem a leitura dos parâmetros do tanque.
2. Um gateway valida e transmite os dados por MQTT.
3. O backend armazena a telemetria e calcula indicadores.
4. O módulo analítico compara a leitura com limites e padrões históricos.
5. O dashboard apresenta o estado do sistema.
6. Eventos críticos geram registro e notificação conforme o protocolo local.

## Critérios para uma prova de conceito

- Sensor calibrado e identificado;
- Dados de teste reproduzíveis;
- Registro de falhas de comunicação;
- Histórico de leituras;
- Limites configuráveis;
- Testes de falso positivo e falso negativo;
- Procedimento de validação por profissional habilitado.

## Próximos entregáveis

- Modelo de dados da telemetria;
- Simulador de sensores;
- Serviço de ingestão MQTT;
- Dashboard mínimo;
- Relatório de anomalias;
- Plano de testes em ambiente controlado.

