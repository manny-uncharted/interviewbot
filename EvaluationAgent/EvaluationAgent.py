from agency_swarm.agents import Agent
from agency_swarm.tools import CodeInterpreter

class EvaluationAgent(Agent):
    def __init__(self):
        super().__init__(
            name="EvaluationAgent",
            description="The EvaluationAgent evaluates and scores candidate responses in real-time using an LLM and the provided Candidate_Criteria_Sheet.xlsx. It analyzes each response for relevance, accuracy, and completeness, scores responses based on predefined criteria, and stores scores and feedback in a structured JSON file for each candidate.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[CodeInterpreter],
            tools_folder="./tools",
            temperature=0.3,
            max_prompt_tokens=25000,
        )
        
    def response_validator(self, message):
        return message
