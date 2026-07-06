import streamlit as st

from agents.orchestrator import Orchestrator

st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="📚",
    layout="wide"
)

st.title("📚 AI Study Assistant")
st.write("Upload a PDF and let AI help you study.")

uploaded_file = st.file_uploader(
    "Upload your PDF",
    type=["pdf"]
)

if uploaded_file:

    orchestrator = Orchestrator()

    text = orchestrator.process_pdf(uploaded_file)

    st.success("PDF Loaded Successfully!")

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "📝 Summary",
            "❓ Quiz",
            "📅 Study Plan",
            "💬 Tutor"
        ]
    )

    with tab1:

        if st.button("Generate Summary"):

            with st.spinner("Generating Summary..."):

                result = orchestrator.summary.run(text)

                st.write(result)

    with tab2:

        if st.button("Generate Quiz"):

            with st.spinner("Generating Quiz..."):

                result = orchestrator.quiz.run(text)

                st.write(result)

    with tab3:

        if st.button("Generate Study Plan"):

            with st.spinner("Generating Plan..."):

                result = orchestrator.planner.run(text)

                st.write(result)

    with tab4:

        question = st.text_input(
            "Ask anything about the PDF"
        )

        if st.button("Ask Tutor"):

            with st.spinner("Thinking..."):

                answer = orchestrator.tutor.run(
                    text,
                    question
                )

                st.write(answer)