from agency_swarm.agents import Agent


class FeedbackAnalyzer(Agent):
    def __init__(self):
        super().__init__(
            name="FeedbackAnalyzer",
            description="The Feedback Analyzer analyzes candidate responses and provides real-time assessment and feedback based on predefined criteria within the InterviewBotAgency.",
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
