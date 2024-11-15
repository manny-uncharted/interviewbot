from agency_swarm.tools import BaseTool
from pydantic import Field

class FeedbackGenerator(BaseTool):
    """
    A tool to generate feedback for candidates based on assessment results.
    It provides constructive feedback, highlighting strengths and areas for improvement, ensuring clarity and actionability.
    """

    criteria_descriptions: dict = Field(
        ..., description="A dictionary of criteria with descriptions for feedback generation."
    )

    def generate_feedback(self, total_score: int, areas_of_improvement: list):
        """
        Generate feedback for a candidate based on their assessment results.
        
        :param total_score: The total score of the candidate's response.
        :param areas_of_improvement: A list of criteria where the candidate needs improvement.
        :return: A string containing the generated feedback.
        """
        feedback = []

        # Provide overall performance feedback
        if total_score >= 80:
            feedback.append("Excellent performance! You have demonstrated strong capabilities.")
        elif total_score >= 60:
            feedback.append("Good performance! You have shown solid skills with room for improvement.")
        else:
            feedback.append("Needs improvement. Focus on enhancing your skills in key areas.")

        # Highlight strengths
        strengths = [criterion for criterion in self.criteria_descriptions if criterion not in areas_of_improvement]
        if strengths:
            feedback.append("Strengths: " + ", ".join([self.criteria_descriptions[criterion] for criterion in strengths]))

        # Highlight areas for improvement
        if areas_of_improvement:
            feedback.append("Areas for Improvement: " + ", ".join([self.criteria_descriptions[criterion] for criterion in areas_of_improvement]))
            feedback.append("Consider focusing on these areas to enhance your performance.")

        return " ".join(feedback)

    def run(self):
        """
        This method is not used in this tool as the functionality is split into specific methods.
        """
        pass