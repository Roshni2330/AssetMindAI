import streamlit as st
import os
import matplotlib.pyplot as plt
import networkx as nx

from rag import extract_text_from_pdf, ask_gemini
from extractor import extract_entities
from graph import create_graph

st.set_page_config(
    page_title="AssetMind AI",
    layout="wide"
)

st.title("🏭 AssetMind AI")
st.markdown(
    "### AI-Powered Industrial Knowledge Intelligence Platform"
)

# Create documents folder
if not os.path.exists("documents"):
    os.makedirs("documents")

# Upload PDF
uploaded_file = st.file_uploader(
    "Upload Industrial PDF",
    type=["pdf"]
)

if uploaded_file:

    # Save PDF
    save_path = os.path.join(
        "documents",
        uploaded_file.name
    )

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(
        f"PDF Saved Successfully: {uploaded_file.name}"
    )

    # Extract text
    pdf_text = extract_text_from_pdf(save_path)

    # Extract entities
    entities = extract_entities(pdf_text)

    st.write("Text Length:", len(pdf_text))

    # ==========================
    # KPI CARDS
    # ==========================

    k1, k2, k3 = st.columns(3)

    k1.metric(
        "Equipment",
        len(entities["equipment"])
    )

    k2.metric(
        "Issues",
        len(entities["issues"])
    )

    k3.metric(
        "Engineers",
        len(entities["engineers"])
    )

    # ==========================
    # INDUSTRIAL INSIGHTS
    # ==========================

    st.subheader("📊 Industrial Insights")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("### Equipment")
        for item in entities["equipment"]:
            st.write("⚙️", item)

    with col2:
        st.write("### Issues")
        for item in entities["issues"]:
            st.write("🚨", item)

    with col3:
        st.write("### Engineers")
        for item in entities["engineers"]:
            st.write("👨‍🔧", item)

    # ==========================
    # KNOWLEDGE GRAPH
    # ==========================

    st.subheader("🕸 Knowledge Graph")

    graph = create_graph(entities)

    fig, ax = plt.subplots(figsize=(8, 5))

    nx.draw(
        graph,
        with_labels=True,
        node_size=2500,
        font_size=9,
        ax=ax
    )

    st.pyplot(fig)

    # ==========================
    # DOCUMENT PREVIEW
    # ==========================

    st.subheader("📄 Document Content")

    st.text_area(
        "Document Preview",
        pdf_text[:3000],
        height=250
    )

    # ==========================
    # OPERATIONS COPILOT
    # ==========================

    st.subheader("🤖 Operations Copilot")

    question = st.text_input(
        "Ask a question about this document"
    )

    if question:

        answer = ask_gemini(
            pdf_text,
            question
        )

        st.subheader("AI Answer")

        st.write(answer)