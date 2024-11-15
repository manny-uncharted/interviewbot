from agency_swarm.tools import BaseTool
from pydantic import Field
import numpy as np

class AssessmentAlgorithm(BaseTool):
    """
    A tool to implement algorithms for assessing candidate responses based on predefined criteria.
    It evaluates the quality of responses, assigns scores, and identifies areas of improvement, supporting data-driven evaluations.
    """

    criteria_weights: dict = Field(
        ..., description="A dictionary of criteria and their corresponding weights for evaluation."
    )

    def evaluate_response(self, response: str, criteria_scores: dict):
        """
        Evaluate the quality of a candidate's response based on predefined criteria and assign a score.
        
        :param response: The candidate's response to be evaluated.
        :param criteria_scores: A dictionary of scores for each criterion.
        :return: A tuple containing the total score and areas of improvement.
        """
        total_score = 0
        areas_of_improvement = []

        for criterion, weight in self.criteria_weights.items():
            score = criteria_scores.get(criterion, 0)
            weighted_score = score * weight
            total_score += weighted_score

            if score < 3:  # Assuming a score scale of 1 to 5
                areas_of_improvement.append(criterion)

        return total_score, areas_of_improvement

    def assign_scores(self, responses: list, criteria_scores_list: list):
        """
        Assign scores to a list of candidate responses based on predefined criteria.
        
        :param responses: A list of candidate responses.
        :param criteria_scores_list: A list of dictionaries containing scores for each criterion for each response.
        :return: A list of tuples containing total scores and areas of improvement for each response.
        """
        results = []
        for response, criteria_scores in zip(responses, criteria_scores_list):
            total_score, areas_of_improvement = self.evaluate_response(response, criteria_scores)
            results.append((total_score, areas_of_improvement))
        return results

    def run(self):
        """
        This method is not used in this tool as the functionality is split into specific methods.
        """
        pass