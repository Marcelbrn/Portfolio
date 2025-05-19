# ===== Importação bibliotecas ===== #
import streamlit as st
from PIL import Image

# ===== Definindo função para gerar estilo css personalizado da página ===== #
def load_css(v_path_css):
    with open(v_path_css, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
# ===== Definindo função para gerar quadro de habilidades técnicas ===== #
def technical_skills(v_habilidades):
    st.markdown("### 🛠️ Habilidades Técnicas")

    cols = st.columns(4, gap="small")
    for idx, (title, items) in enumerate(v_habilidades.items()):
        with cols[idx]:
            v_lista_habilidades = "".join(f"<li>{item}</li>" for item in items)

            st.markdown(f"""
                            <div class="skill-card">
                                <h5>{title}</h5>
                                <ul>{v_lista_habilidades}</ul>
                            </div><br>
                        """, unsafe_allow_html=True)
