from agency_swarm.agents import Agent


class InterviewCoordinator(Agent):
    def __init__(self):
        super().__init__(
            name="InterviewCoordinator",
            description="The InterviewCoordinator agent manages the overall interview flow and candidate interactions. It starts with a warm and welcome greeting once the page loads and introduces the candidate to the interview format, controls the sequence of questions and phases, adapts questions based on candidate responses, and summarizes the interview outcome. It uses Gradio UI for the frontend interface and communicates with the EvaluationAgent and KnowledgeRetrievalAgent.",
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
