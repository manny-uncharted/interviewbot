from agency_swarm.tools import BaseTool
from pydantic import Field
import os
import json

class JSONDataStorage(BaseTool):
    """
    A tool to store candidate scores and other relevant data in a structured JSON format within the 'candidates' folder.
    It can create, read, update, and delete JSON files, ensuring data integrity and accessibility.
    """

    folder_path: str = Field(
        "candidates", description="The folder path where JSON files are stored."
    )

    def __post_init__(self):
        # Ensure the folder exists
        os.makedirs(self.folder_path, exist_ok=True)

    def create_json_file(self, candidate_id: str, data: dict):
        """
        Create a JSON file for a candidate with the given data.
        """
        file_path = os.path.join(self.folder_path, f"{candidate_id}.json")
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        return f"JSON file created for candidate {candidate_id}."

    def read_json_file(self, candidate_id: str):
        """
        Read and return the data from a candidate's JSON file.
        """
        file_path = os.path.join(self.folder_path, f"{candidate_id}.json")
        if os.path.exists(file_path):
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
            return data
        else:
            return f"JSON file for candidate {candidate_id} does not exist."

    def update_json_file(self, candidate_id: str, new_data: dict):
        """
        Update a candidate's JSON file with new data.
        """
        file_path = os.path.join(self.folder_path, f"{candidate_id}.json")
        if os.path.exists(file_path):
            with open(file_path, 'r+') as json_file:
                data = json.load(json_file)
                data.update(new_data)
                json_file.seek(0)
                json.dump(data, json_file, indent=4)
                json_file.truncate()
            return f"JSON file for candidate {candidate_id} updated."
        else:
            return f"JSON file for candidate {candidate_id} does not exist."

    def delete_json_file(self, candidate_id: str):
        """
        Delete a candidate's JSON file.
        """
        file_path = os.path.join(self.folder_path, f"{candidate_id}.json")
        if os.path.exists(file_path):
            os.remove(file_path)
            return f"JSON file for candidate {candidate_id} deleted."
        else:
            return f"JSON file for candidate {candidate_id} does not exist."

    def run(self):
        """
        This method is not used in this tool as the functionality is split into specific methods.
        """
        pass