from agency_swarm.tools import BaseTool
from pydantic import Field

class CandidateInteractionTool(BaseTool):
    """
    This tool handles greeting the candidate and introducing them to the interview format.
    It provides a welcoming message and outlines the structure of the interview to set the candidate at ease.
    """

    candidate_name: str = Field(
        ..., description="The name of the candidate to personalize the greeting."
    )
    interview_structure: str = Field(
        ..., description="A brief description of the interview structure."
    )

    def run(self):
        """
        Provides a welcoming message and outlines the interview structure.
        """
        welcome_message = (
            f"Hello {self.candidate_name},\n\n"
            "Welcome to the interview process. We are excited to have you here today.\n\n"
            "Interview Structure:\n"
            f"{self.interview_structure}\n\n"
            "Please feel free to ask any questions before we begin. We wish you the best of luck!"
        )

        return welcome_message


