from agency_swarm.tools import BaseTool
from pydantic import Field
from typing import List, Dict

class ScoringTool(BaseTool):
    """
    This tool applies the extracted criteria to score candidate responses.
    It takes the evaluation results from the LLM and the criteria from the CriteriaSheetParserTool
    to calculate a final score for each response.
    """

    evaluation_results: Dict[str, float] = Field(
        ..., description="The evaluation results from the LLM, with criteria as keys and scores as values."
    )
    criteria: List[str] = Field(
        ..., description="The list of criteria extracted from the CriteriaSheetParserTool."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method calculates a final score for each response based on the evaluation results and criteria.
        """
        total_score = 0
        max_score = len(self.criteria)  # Assuming each criterion contributes equally to the final score

        for criterion in self.criteria:
            score = self.evaluation_results.get(criterion, 0)
            total_score += score
            print(f"Criterion: {criterion}, Score: {score}")

        final_score = (total_score / max_score) * 100  # Calculate percentage score
        print(f"Final Score: {final_score}%")
        return final_score

# # Example usage
# if __name__ == "__main__":
#     tool = ScoringTool(
#         evaluation_results={
#             "Relevance": 0.8,
#             "Accuracy": 0.9,
#             "Completeness": 0.7
#         },
#         criteria=["Relevance", "Accuracy", "Completeness"]
#     )
#     tool.run()



# from agency_swarm.tools import BaseTool
# from pydantic import Field
# from typing import List, Dict

# class ScoringTool(BaseTool):
#     """
#     This tool calculates a final score for the candidate based on LLM-provided scores for each criterion.
#     """

#     evaluation_results: Dict[str, float] = Field(
#         ..., description="Dictionary with criteria as keys and scores (0 to 1) as values."
#     )

#     def run(self):
#         total_score = sum(self.evaluation_results.values())
#         max_score = len(self.evaluation_results)
#         final_score = (total_score / max_score) * 100  # Calculate percentage

#         return final_score

# # Example usage
# if __name__ == "__main__":
#     tool = ScoringTool(
#         evaluation_results={
#             "Relevance": 0.8,
#             "Accuracy": 0.9,
#             "Completeness": 0.7
#         }
#     )
#     print(f"Final Score: {tool.run()}%")
