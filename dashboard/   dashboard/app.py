import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Configuração da página
st.set_page_config(
    page_title="AI-CryoDiag | Monitoramento Criogênico SUS",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilização profissional
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #003366;
        font-weight: bold;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #555;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f8f9fa;
        padding: 1.2rem;
        border-radius: 0.5rem;
        border-left: 5px solid #003366;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho
st.markdown('<div class="main-header">🧊 AI-CryoDiag</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Sistema de Diagnóstico Preditivo para Armazenamento Criogênico — SUS</div>', unsafe_allow_html=True)

# Simulação de dados em tempo real
@st.cache_data
def gerar_dados_demo():
    horas = pd.date_range(end=datetime.now(), periods=50, freq='5min')
    np.random.seed(42)
    nivel = np.clip(np.random.normal(75, 3, 50), 60, 90)
    pressao = np.clip(np.random.normal(12.0, 0.5, 50), 10, 14)
    temperatura = np.clip(np.random.normal(-183, 1.5, 50), -190, -175)
    # Injetar anomalia recente
    nivel[-5:] -= np.linspace(5, 15, 5)
    pressao[-5:] -= np.linspace(1, 4, 5)
    return pd.DataFrame({
        'timestamp': horas,
        'nivel_percent': nivel,
        'pressao_bar': pressao,
        'temperatura_c': temperatura
    })

df = gerar_dados_demo()

ultimo_nivel = df['nivel_percent'].iloc[-1]
ultima_pressao = df['pressao_bar'].iloc[-1]
ultima_temp = df['temperatura_c'].iloc[-1]

anomalia_detectada = ultimo_nivel < 65 or ultima_pressao < 10.5

# Barra lateral
with st.sidebar:
    st.image("https://raw.githubusercontent.com/acelinodomingos/AI-CryoDiag/main/AI-CryoDiag-logo.png", width=200)
    st.markdown("### ⚙️ Controles")
    tanque_selecionado = st.selectbox("Tanque", ["TQ-01 (Oxigênio)", "TQ-02 (Nitrogênio)"])
    atualizacao = st.slider("Atualização (segundos)", 1, 10, 5)
    st.markdown("---")
    st.info("**Autor:** Acelino D. C. Filho\nGestor Público | INCA/RJ\nIA Aplicada à Saúde")

# Alerta de Segurança
if anomalia_detectada:
    st.error("🚨 **ALERTA CRÍTICO:** Queda anormal de nível e pressão detectada! Risco de interrupção no fornecimento. Acionar protocolo de reposição de emergência.")
else:
    st.success("✅ **SISTEMA NORMAL:** Parâmetros dentro dos limites operacionais de segurança.")

# KPIs
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("📊 Nível do Tanque", f"{ultimo_nivel:.1f}%", f"{ultimo_nivel - df['nivel_percent'].iloc[-2]:.1f}%")
    st.markdown('</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("🔵 Pressão", f"{ultima_pressao:.2f} bar", f"{ultima_pressao - df['pressao_bar'].iloc[-2]:.2f} bar")
    st.markdown('</div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("🌡️ Temperatura", f"{ultima_temp:.1f} °C", f"{ultima_temp - df['temperatura_c'].iloc[-2]:.1f} °C")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# Gráficos
col1, col2 = st.columns(2)
with col1:
    st.subheader("📈 Histórico de Nível (%)")
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=df['timestamp'], y=df['nivel_percent'], mode='lines+markers', line=dict(color='#003366', width=3)))
    fig1.add_hline(y=65, line_dash="dash", line_color="red", annotation_text="Limite Crítico")
    fig1.update_layout(height=350)
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("📉 Histórico de Pressão (bar)")
    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=df['timestamp'], y=df['pressao_bar'], mode='lines+markers', line=dict(color='#0066cc', width=3)))
    fig2.add_hline(y=10.5, line_dash="dash", line_color="red", annotation_text="Limite Crítico")
    fig2.update_layout(height=350)
    st.plotly_chart(fig2, use_container_width=True)

# Rodapé
st.markdown("---")
st.caption("AI-CryoDiag v1.0 | Rede de fármacos gasosos do SUS | Dados simulados para demonstração.")
