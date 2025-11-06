import streamlit as st

st.title("🧠 Zanini Renk - Controle de Mancais")
st.write("""
Este é o protótipo do aplicativo para integração entre:
- Técnico de campo
- Engenharia
- Pré-usinagem
""")

st.subheader("Fluxo básico:")
st.markdown("""
1. O técnico preenche os dados de campo.
2. A engenharia revisa e autoriza a pré-usinagem.
3. O leitor final consulta se está **AUTORIZADO**, **NEGADO** ou **PENDENTE**.
""")

st.info("App base pronto. Em seguida vamos adicionar o banco de dados e os dashboards.")
