import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

def gerar_dados_criogenicos(dias=30, intervalo_minutos=15):
    """
    Gera dados sintéticos de telemetria para tanques criogênicos (O2 e N2).
    Simula comportamento normal e anomalias (queda de pressão, vazamento).
    """
    print("🧊 Iniciando geração de dados sintéticos criogênicos...")
    
    # Configurações
    total_registros = dias * 24 * (60 // intervalo_minutos)
    start_time = datetime.now() - timedelta(days=dias)
    
    # Gerar timestamps
    timestamps = [start_time + timedelta(minutes=i*intervalo_minutos) for i in range(total_registros)]
    
    # Simular dados base (com ruído normal)
    np.random.seed(42) # Para reprodutibilidade
    nivel_litros = np.random.normal(loc=8000, scale=500, size=total_registros) # Capacidade ~10000L
    pressao_psi = np.random.normal(loc=150, scale=10, size=total_registros)
    temperatura_c = np.random.normal(loc=-183, scale=2, size=total_registros) # Ponto de ebulição do O2
    
    # Injetar anomalias aleatórias (ex: 2% de chance de vazamento/queda de pressão)
    anomalias = np.random.choice([0, 1], size=total_registros, p=[0.98, 0.02])
    
    # Se houver anomalia, simula queda brusca de nível e pressão
    nivel_litros = np.where(anomalias == 1, nivel_litros - np.random.uniform(1000, 2000, total_registros), nivel_litros)
    pressao_psi = np.where(anomalias == 1, pressao_psi - np.random.uniform(30, 50, total_registros), pressao_psi)
    
    # Criar DataFrame
    df = pd.DataFrame({
        'timestamp': timestamps,
        'tanque_id': ['TQ-01'] * total_registros,
        'nivel_litros': np.round(nivel_litros, 2),
        'pressao_psi': np.round(pressao_psi, 2),
        'temperatura_c': np.round(temperatura_c, 2),
        'is_anomalia': anomalias
    })
    
    # Garantir que níveis não fiquem negativos
    df['nivel_litros'] = df['nivel_litros'].clip(lower=0)
    df['pressao_psi'] = df['pressao_psi'].clip(lower=0)
    
    # Salvar em CSV
    caminho_saida = '../data/dados_telemetria_sintetica.csv'
    os.makedirs('../data', exist_ok=True)
    df.to_csv(caminho_saida, index=False, encoding='utf-8')
    
    print(f"✅ Sucesso! {len(df)} registros gerados e salvos em: {caminho_saida}")
    print(f"⚠️ Anomalias detectadas: {df['is_anomalia'].sum()} ({(df['is_anomalia'].mean()*100):.1f}%)")
    
    return df

if __name__ == "__main__":
    # Executa a geração de 30 dias de dados a cada 15 minutos
    df_gerado = gerar_dados_criogenicos(dias=30, intervalo_minutos=15)
    print("\nAmostra dos dados gerados:")
    print(df_gerado.head())
