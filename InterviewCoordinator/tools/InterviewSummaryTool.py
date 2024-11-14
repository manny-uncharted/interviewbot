from agency_swarm.tools import BaseTool
from pydantic import Field

class InterviewSummaryTool(BaseTool):
    """
    This tool summarizes the interview outcome. It compiles key points from the interview,
    including candidate strengths, areas for improvement, and overall performance.
    The summary is concise and informative.
    """

    candidate_name: str = Field(
        ..., description="The name of the candidate being summarized."
    )
    strengths: str = Field(
        ..., description="A summary of the candidate's strengths observed during the interview."
    )
    areas_for_improvement: str = Field(
        ..., description="A summary of the areas where the candidate can improve."
    )
    overall_performance: str = Field(
        ..., description="An overall assessment of the candidate's performance."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method compiles the interview summary based on the provided details.
        """
        summary = (
            f"Interview Summary for {self.candidate_name}:\n\n"
            "Strengths:\n"
            f"{self.strengths}\n\n"
            "Areas for Improvement:\n"
            f"{self.areas_for_improvement}\n\n"
            "Overall Performance:\n"
            f"{self.overall_performance}\n"
        )

        print(summary)
        return "Interview summary compiled successfully"

