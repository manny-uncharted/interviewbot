import unittest
from unittest.mock import patch, MagicMock
from KnowledgeRetrievalAgent.tools.ClarificationRequestHandlerTool import ClarificationRequestHandlerTool
from KnowledgeRetrievalAgent.tools.DocumentParserIndexerTool import DocumentParserIndexerTool
from KnowledgeRetrievalAgent.tools.InformationSupplierTool import InformationSupplierTool
from KnowledgeRetrievalAgent.tools.WebScraperDataIngestionTool import WebScraperDataIngestionTool

class TestClarificationRequestHandlerTool(unittest.TestCase):
    @patch('openai.Embedding.create')
    @patch('pinecone.Index.query')
    def test_run(self, mock_query, mock_embedding):
        mock_embedding.return_value = {'data': [{'embedding': [0.1, 0.2, 0.3]}]}
        mock_query.return_value = {
            'matches': [
                {'id': 'doc1', 'score': 0.95, 'metadata': {'title': 'Global Warming'}}
            ]
        }
        
        tool = ClarificationRequestHandlerTool(query="What is global warming?")
        result = tool.run()
        self.assertIn("Top relevant documents", result)
        self.assertIn("Document ID: doc1", result)



class TestDocumentParserIndexerTool(unittest.TestCase):
    @patch('PyPDF2.PdfReader')
    @patch('docx.Document')
    @patch('json.dump')
    def test_run(self, mock_json_dump, mock_docx, mock_pdf_reader):
        mock_pdf_reader.return_value.pages = [MagicMock(extract_text=MagicMock(return_value="PDF content"))]
        mock_docx.return_value.paragraphs = [MagicMock(text="Docx content")]

        tool = DocumentParserIndexerTool(
            document_paths=["InterviewBot/KnowledgeRetrievalAgent/files/cursorrules_file-A7a36Gw2LgwbqKVGXFW2VeOy.txt"],
            index_file_path="index.json"
        )
        with patch('builtins.open', unittest.mock.mock_open()):
            result = tool.run()
        
        self.assertEqual(result, "Index has been created and saved to index.json")



class TestInformationSupplierTool(unittest.TestCase):
    @patch('openai.Embedding.create')
    @patch('pinecone.Index.query')
    def test_run(self, mock_query, mock_embedding):
        mock_embedding.return_value = {'data': [{'embedding': [0.1, 0.2, 0.3]}]}
        mock_query.return_value = {
            'matches': [
                {'id': 'doc1', 'score': 0.88, 'metadata': {'topic': 'Renewable Energy'}}
            ]
        }

        tool = InformationSupplierTool(query="Tell me about renewable energy.")
        result = tool.run()
        self.assertIn("Pertinent information for the InterviewCoordinator", result)
        self.assertIn("Document ID: doc1", result)



class TestWebScraperDataIngestionTool(unittest.TestCase):
    @patch('requests.get')
    @patch('openai.Embedding.create')
    @patch('pinecone.Index.upsert')
    def test_run(self, mock_upsert, mock_embedding, mock_requests_get):
        # Mocking file reading
        with patch('builtins.open', unittest.mock.mock_open(read_data="https://example.com\n")):
            mock_requests_get.return_value.content = "<html><body>Sample content</body></html>"
            mock_embedding.return_value = {'data': [{'embedding': [0.1, 0.2, 0.3]}]}

            tool = WebScraperDataIngestionTool(urls_file_path="urls.txt")
            result = tool.run()
        
        self.assertEqual(result, "Data has been scraped, converted to embeddings, and stored in Pinecone.")

# Run the tests
if __name__ == "__main__":
    unittest.main()
