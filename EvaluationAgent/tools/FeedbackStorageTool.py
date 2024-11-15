# from agency_swarm.tools import BaseTool
# from pydantic import Field
# import json
# import os

# class FeedbackStorageTool(BaseTool):
#     """
#     This tool stores scores and feedback in a structured JSON file for each candidate.
#     It takes the candidate's name, scores, and feedback, and saves them in a JSON format,
#     ensuring data is organized and easily retrievable.
#     """

#     candidate_name: str = Field(
#         ..., description="The name of the candidate."
#     )
#     scores: float = Field(
#         ..., description="The final score of the candidate."
#     )
#     feedback: str = Field(
#         ..., description="The feedback for the candidate."
#     )
#     file_path: str = Field(
#         ..., description="The file path to store the JSON data."
#     )

#     def run(self):
#         """
#         The implementation of the run method, where the tool's main functionality is executed.
#         This method stores the candidate's scores and feedback in a JSON file.
#         """
#         # Create a dictionary to store the candidate's data
#         candidate_data = {
#             "name": self.candidate_name,
#             "scores": self.scores,
#             "feedback": self.feedback
#         }

#         # Check if the file already exists
#         if os.path.exists(self.file_path):
#             # Load existing data
#             with open(self.file_path, 'r') as file:
#                 data = json.load(file)
#         else:
#             # Initialize an empty list if the file does not exist
#             data = []

#         # Append the new candidate data
#         data.append(candidate_data)

#         # Write the updated data back to the file
#         with open(self.file_path, 'w') as file:
#             json.dump(data, file, indent=4)

#         print(f"Data for {self.candidate_name} has been stored successfully.")
#         return f"Data for {self.candidate_name} has been stored successfully."


from agency_swarm.tools import BaseTool
from pydantic import Field
import json
import os

# Default file path for storing feedback data
DEFAULT_FILE_PATH = "./candidates/candidates.json"

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
        DEFAULT_FILE_PATH, description="The file path to store the JSON data. Defaults to 'feedback_data.json'."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method stores the candidate's scores and feedback in a JSON file.
        """
        # Ensure the directory exists
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

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
