from agency_swarm.tools import BaseTool
from pydantic import Field

class InterviewFlowManagerTool(BaseTool):
    """
    This tool manages the sequence of questions and phases during the interview.
    It adapts questions based on candidate responses, ensuring a smooth and logical
    flow of the interview process.
    """

    initial_question: str = Field(
        ..., description="The initial question to start the interview."
    )
    follow_up_questions: dict = Field(
        ..., description="A dictionary mapping keywords in responses to follow-up questions."
    )

    def run(self):
        """
        Manages the flow of the interview by adapting questions based on responses.
        """
        current_question = self.initial_question
        print(f"Starting Interview: {current_question}")

        while True:
            response = input("Candidate Response: ").strip().lower()
            matched = False

            # Check if any keyword in follow-up questions matches the response
            for keyword, follow_up in self.follow_up_questions.items():
                if keyword in response:
                    current_question = follow_up
                    print(f"Next Question: {current_question}")
                    matched = True
                    break

            # If no match is found, break out of the loop
            if not matched:
                print("No suitable follow-up question found for this response.")
                break

        return "Interview process completed"


