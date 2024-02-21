import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)


def calcular_esforcos_internos(L, E, A, Q):
    x = np.linspace(0, L, 1000)  # Pontos ao longo do comprimento da viga
    w = Q * x / 2  # Função de carga distribuída

    # Reações de apoio
    R1 = Q * L / 2
    R2 = Q * L / 2

    V = R1 - Q * x  # Esforço cortante
    M = R1 * x - (Q * x ** 2) / 2  # Momento fletor

    # Plotar os esforços internos
    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)
    plt.plot(x, V)
    plt.title('Esforço Cortante')
    plt.xlabel('Posição ao longo da viga')
    plt.ylabel('Esforço Cortante (N)')
    plt.grid(True)
    plt.xlim(0, L)  # Limites do eixo x
    plt.text(0, R1, 'Apoio 1', fontsize=10, ha='right')
    plt.text(L, R2, 'Apoio 2', fontsize=10, ha='left')

    plt.subplot(2, 1, 2)
    plt.plot(x, M)
    plt.title('Momento Fletor')
    plt.xlabel('Posição ao longo da viga')
    plt.ylabel('Momento Fletor (Nm)')
    plt.grid(True)
    plt.xlim(0, L)  # Limites do eixo x
    plt.text(0, 0, 'Apoio 1', fontsize=10, ha='right')
    plt.text(L, 0, 'Apoio 2', fontsize=10, ha='left')

    st.pyplot()


def main():
    st.title('Cálculo de Esforços Internos em uma Viga Biapoiada')

    # Entradas do usuário
    L = st.number_input('Comprimento da viga (m)', min_value=0.1, step=0.1, value=1.0)
    E = st.number_input('Módulo de Elasticidade (Pa)', min_value=1e9, step=1e9, value=2.1e11)
    A = st.number_input('Área da seção transversal (m^2)', min_value=0.01, step=0.01, value=0.1)
    Q = st.number_input('Carga distribuída (N/m)', min_value=0.0, step=100.0, value=1000.0)

    # Calcular esforços internos quando o botão for pressionado
    if st.button('Calcular Esforços Internos'):
        calcular_esforcos_internos(L, E, A, Q)
    if st.button('Limpar formulário'):
        st.empty()


if __name__ == "__main__":
    main()
