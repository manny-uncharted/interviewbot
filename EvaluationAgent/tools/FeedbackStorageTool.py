from agency_swarm.tools import BaseTool
from pydantic import Field
import json
import os

class FeedbackStorageTool(BaseTool):
    """
    This tool stores scores and feedback in a structured JSON file for each candidate.
    It takes the candidate's name, scores, and feedback, and saves them in a JSON format,
    ensuring data is organized and easily retrievable.
    """

    candidate_name: str = Field(
        ..., description="The name of the candidate."
    )
    scores: float = Field(
        ..., description="The final score of the candidate."
    )
    feedback: str = Field(
        ..., description="The feedback for the candidate."
    )
    file_path: str = Field(
        ..., description="The file path to store the JSON data."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method stores the candidate's scores and feedback in a JSON file.
        """
        # Create a dictionary to store the candidate's data
        candidate_data = {
            "name": self.candidate_name,
            "scores": self.scores,
            "feedback": self.feedback
        }

        # Check if the file already exists
        if os.path.exists(self.file_path):
            # Load existing data
            with open(self.file_path, 'r') as file:
                data = json.load(file)
        else:
            # Initialize an empty list if the file does not exist
            data = []

        # Append the new candidate data
        data.append(candidate_data)

        # Write the updated data back to the file
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)

        print(f"Data for {self.candidate_name} has been stored successfully.")
        return f"Data for {self.candidate_name} has been stored successfully."

# # Example usage
# if __name__ == "__main__":
#     tool = FeedbackStorageTool(
#         candidate_name="John Doe",
#         scores=85.0,
#         feedback="The candidate demonstrated strong analytical skills.",
#         file_path="candidate_feedback.json"
#     )
#     tool.run()


# from agency_swarm.tools import BaseTool
# from pydantic import Field
# import json
# import os

# class FeedbackStorageTool(BaseTool):
#     """
#     Stores the candidate's score and feedback in a JSON file.
#     """

#     candidate_name: str = Field(..., description="Name of the candidate.")
#     final_score: float = Field(..., description="The calculated final score for the candidate.")
#     feedback: str = Field(..., description="Summary feedback for the candidate.")
#     file_path: str = Field(..., description="The file path to store the JSON data.")

#     def run(self):
#         candidate_data = {
#             "name": self.candidate_name,
#             "final_score": self.final_score,
#             "feedback": self.feedback
#         }

#         data = []
#         if os.path.exists(self.file_path):
#             with open(self.file_path, 'r') as file:
#                 data = json.load(file)

#         data.append(candidate_data)

#         with open(self.file_path, 'w') as file:
#             json.dump(data, file, indent=4)

#         return f"Feedback and score stored for {self.candidate_name}."

