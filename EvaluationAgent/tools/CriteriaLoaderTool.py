from agency_swarm.tools import BaseTool
from pydantic import Field
import pandas as pd
import os

class CriteriaLoaderTool(BaseTool):
    """
    This tool loads evaluation criteria from the Candidate_Criteria_Sheet.csv file.
    """

    file_path: str = Field(
        ..., description="The path to the Candidate_Criteria_Sheet.csv file."
    )

    def run(self):
        if not os.path.exists(self.file_path):
            return f"Error: File {self.file_path} not found."

        try:
            df = pd.read_csv(self.file_path)
            if 'Criteria' not in df.columns:
                return "Error: 'Criteria' column not found in the file."
            
            criteria_list = df['Criteria'].dropna().tolist()
            return {"criteria": criteria_list}
        except Exception as e:
            return f"Error loading criteria: {str(e)}"

