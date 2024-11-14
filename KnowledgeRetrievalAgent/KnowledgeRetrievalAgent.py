from agency_swarm.agents import Agent


class KnowledgeRetrievalAgent(Agent):
    def __init__(self):
        super().__init__(
            name="KnowledgeRetrievalAgent",
            description="The KnowledgeRetrievalAgent retrieves relevant information from the knowledge base to assist with context-specific questions. It scrapes data from specified URLs in urls.txt and additional files like cursorrules.txt, adds them to the Pinecone vector database using OpenAI's embedding models. It parses and indexes documents, handles requests for clarifications or topic-specific information, and dynamically supplies the InterviewCoordinator with pertinent information for deeper interview questions.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[],
            tools_folder="./tools",
            temperature=0.3,
            max_prompt_tokens=25000,
        )
        
    def response_validator(self, message):
        return message
