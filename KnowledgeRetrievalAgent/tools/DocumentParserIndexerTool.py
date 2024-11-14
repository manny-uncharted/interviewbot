from agency_swarm.tools import BaseTool
from pydantic import Field
import os
import json
from typing import List
from sklearn.feature_extraction.text import TfidfVectorizer
import PyPDF2
import docx
# import textract

class DocumentParserIndexerTool(BaseTool):
    """
    This tool parses and indexes documents for efficient searching and retrieval.
    It reads various document formats, extracts text content, and creates an index
    for efficient searching and retrieval of relevant information.
    """

    document_paths: List[str] = Field(
        ..., description="A list of file paths to the documents to be parsed and indexed."
    )
    index_file_path: str = Field(
        ..., description="The file path where the index will be saved as a JSON file."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method reads documents, extracts text, and creates an index for efficient searching.
        """
        documents = []

        for path in self.document_paths:
            ext = os.path.splitext(path)[1].lower()
            text = ""

            # try:
            if ext == ".pdf":
                with open(path, 'rb') as file:
                    reader = PyPDF2.PdfReader(file)
                    for page in reader.pages:
                        text += page.extract_text()
            elif ext == ".docx":
                doc = docx.opendocx(path)
                for para in doc.paragraphs:
                    text += para.text
            else:
                with open(path, 'r') as file:
                    content = file.read()
                    # text = textract.process(path).decode('utf-8')

                documents.append(text)
            # except Exception as e:
            #     print(f"Error processing {path}: {e}")

        # Create a TF-IDF vectorizer and fit it to the documents
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(documents)
        feature_names = vectorizer.get_feature_names_out()

        # Create an index dictionary
        index = {
            "documents": documents,
            "tfidf_matrix": tfidf_matrix.toarray().tolist(),
            "feature_names": feature_names.tolist()
        }

        # Save the index to a JSON file
        with open(self.index_file_path, 'w') as file:
            json.dump(index, file)

        print(f"Index has been created and saved to {self.index_file_path}.")
        return f"Index has been created and saved to {self.index_file_path}."

