from agency_swarm.tools import BaseTool
from pydantic import Field
import requests
from bs4 import BeautifulSoup
import openai
from pinecone import Pinecone
import os
from InterviewBot.utils.constants import pinecone_api_key

pinecone = Pinecone(api_key=pinecone_api_key)
index_name = "web-scraper-index"

# Initialize OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

class WebScraperDataIngestionTool(BaseTool):
    urls_file_path: str = Field(
        ..., description="The file path to the text file containing URLs to scrape."
    )

    def run(self):
        # Read URLs from the file
        try:
            with open(self.urls_file_path, 'r') as file:
                urls = file.readlines()
            with open(self.additional_file_path, 'r') as file:
                additional_data = file.read()
        except Exception as e:
            print(f"Error reading file: {e}")
            return

        scraped_data = []
        for url in urls:
            url = url.strip()
            try:
                response = requests.get(url)
                soup = BeautifulSoup(response.content, 'html.parser')
                scraped_data.append(soup.get_text())
            except Exception as e:
                print(f"Error scraping {url}: {e}")

        all_data = scraped_data + [additional_data]
        embeddings = []
        for data in all_data:
            try:
                response = openai.Embedding.create(input=data, model="text-embedding-ada-002")
                embeddings.append(response['data'][0]['embedding'])
            except Exception as e:
                print(f"Error creating embedding: {e}")

        try:
            index = pinecone.Index(index_name)
            for i, embedding in enumerate(embeddings):
                index.upsert([(f"doc-{i}", embedding)])
        except Exception as e:
            print(f"Error upserting to Pinecone: {e}")

        print("Data has been scraped, converted to embeddings, and stored in Pinecone.")
        return "Data has been scraped, converted to embeddings, and stored in Pinecone."

