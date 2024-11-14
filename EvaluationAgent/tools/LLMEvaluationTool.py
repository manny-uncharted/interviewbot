from agency_swarm.tools import BaseTool
from pydantic import Field
import openai
import os

# Set up the OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

class LLMEvaluationTool(BaseTool):
    """
    This tool uses OpenAI's language model to evaluate and score candidate responses based on specified criteria.
    It leverages OpenAI's LLM API to analyze the responses and return evaluation feedback.
    """

    candidate_response: str = Field(
        ..., description="The candidate's response to be evaluated."
    )
    evaluation_criteria: str = Field(
        ..., description="The criteria for evaluating the response, such as relevance, accuracy, and completeness."
    )

    def run(self):
        """
        Evaluates the candidate's response using OpenAI's language model based on the provided criteria.
        """
        # Prepare the prompt for evaluation
        prompt = (
            f"Evaluate the following response based on the criteria provided:\n\n"
            f"Response:\n{self.candidate_response}\n\n"
            f"Evaluation Criteria:\n{self.evaluation_criteria}\n\n"
            "Provide feedback on the response's relevance, accuracy, and completeness."
        )

        # Call OpenAI's completion API for evaluation
        try:
            response = openai.Completion.create(
                model="gpt4-o",
                prompt=prompt,
                max_tokens=150
            )
            evaluation_results = response.choices[0].text.strip()
            print("Evaluation Results:", evaluation_results)
            return evaluation_results
        except Exception as e:
            error_message = f"Failed to evaluate response due to an error: {str(e)}"
            print(error_message)
            return error_message

# # Example usage
# if __name__ == "__main__":
#     tool = LLMEvaluationTool(
#         candidate_response="The candidate's detailed response to the interview question.",
#         evaluation_criteria="Relevance, accuracy, and completeness"
#     )
#     tool.run()


# from agency_swarm.tools import BaseTool
# from pydantic import Field
# import openai
# import os

# openai.api_key = os.getenv("OPENAI_API_KEY")

# class LLMEvaluationTool(BaseTool):
#     """
#     This tool evaluates the candidate's response based on given criteria using OpenAI's language model.
#     """

#     candidate_response: str = Field(..., description="The response provided by the candidate.")
#     criteria: str = Field(..., description="Specific evaluation criteria to use for assessment.")

#     def run(self):
#         prompt = (
#             f"Evaluate the following response according to this criterion:\n\n"
#             f"Response:\n{self.candidate_response}\n\n"
#             f"Criterion:\n{self.criteria}\n\n"
#             "Provide feedback and a score from 0 to 1."
#         )

#         try:
#             response = openai.Completion.create(
#                 model="gpt-4o",
#                 prompt=prompt,
#                 max_tokens=150
#             )
#             feedback = response.choices[0].text.strip()
#             return feedback
#         except Exception as e:
#             return f"Error during LLM evaluation: {str(e)}"


