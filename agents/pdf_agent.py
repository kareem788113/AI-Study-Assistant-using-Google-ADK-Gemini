from utils.pdf_reader import extract_text_from_pdf


class PDFAgent:

    def run(self, uploaded_file):

        text = extract_text_from_pdf(uploaded_file)

        return text