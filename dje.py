import streamlit as st

# Título do app
st.set_page_config(page_title="Pesquisa DJE", page_icon="corina_ico.png")

st.markdown(
    "<h3 style='text-align: center;'>TRT12<br>Corregedoria Regional</h3>", 
    unsafe_allow_html=True
)
st.title("Consulta Painel Domicílio Judicial Eletrônico")

# Input do usuário
proc_completo = st.text_input(label="Digite o número do processo:", placeholder="0000000-00.0000.0.00.0000")
processo = proc_completo.replace('-', '').replace('.', '')

# Montar o link dinâmico
url = f"https://paineisanalytics.cnj.jus.br/single/?appid=205de01d-6bb2-45c3-8be3-a61ea20b9957&sheet=fe35a4b1-ea16-453c-8d29-7bde4e013ec7&theme=horizon&lang=pt-BR&opt=ctxmenu,currsel&select=cpp_numero_processo,{processo}"

# Botão para abrir o link
if st.button("Consultar Processo"):
    # Usando HTML para abrir em nova aba
    st.markdown(f'<a href="{url}" target="_blank">Clique aqui se o link não abrir</a>', unsafe_allow_html=True)
    st.write("Habilite a abertura de pop-up no navegador para as próximas tentativas.")
    
    # Tentativa com JavaScript (pode ser bloqueado por alguns navegadores)
    js = f"""<script>window.open("{url}", "_blank");</script>"""
    st.components.v1.html(js, height=0)

