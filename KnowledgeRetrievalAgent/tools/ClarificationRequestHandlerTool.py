from agency_swarm.tools import BaseTool
from pydantic import Field
import openai
from pinecone import Pinecone
import os
from utils.constants import pinecone_api_key


pinecone = Pinecone(api_key=pinecone_api_key)
index_name = "web-scraper-index"

# Initialize OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

class ClarificationRequestHandlerTool(BaseTool):
    """
    This tool handles requests for clarifications or topic-specific information.
    It searches the indexed documents for relevant data based on a query and returns
    the most pertinent information using the Pinecone vector database.
    """

    query: str = Field(
        ..., description="The query for which clarification or topic-specific information is requested."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method searches the indexed documents for relevant data based on the query.
        """
        # Convert the query to an embedding using OpenAI
        response = openai.Embedding.create(input=self.query, model="text-embedding-ada-002")
        query_embedding = response['data'][0]['embedding']

        # Search the Pinecone index for the most similar documents
        index = pinecone.Index(index_name)
        search_results = index.query(queries=[query_embedding], top_k=3, include_metadata=True)

        # Extract and format the most relevant information
        formatted_info = "Top relevant documents:\n"
        for match in search_results['matches']:
            doc_id = match['id']
            score = match['score']
            metadata = match.get('metadata', {})
            formatted_info += f"Document ID: {doc_id}, Score: {score:.4f}, Metadata: {metadata}\n"

        print(formatted_info)
        return formatted_info

