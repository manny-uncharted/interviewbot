from agency_swarm.tools import BaseTool
from pydantic import Field
import random

class ResponseHandler(BaseTool):
    """
    A tool to handle candidate responses during an interview.
    It interprets and evaluates responses, provides feedback, adjusts questions based on performance, and records responses accurately.
    """

    questions: list = Field(
        ..., description="A list of interview questions."
    )
    responses: dict = Field(
        default_factory=dict, description="A dictionary to store candidate responses with the question as the key."
    )
    feedback: dict = Field(
        default_factory=dict, description="A dictionary to store feedback for each response."
    )
    scores: dict = Field(
        default_factory=dict, description="A dictionary to store scores for each response."
    )
    current_question_index: int = Field(
        0, description="The index of the current question being asked."
    )
    completed_questions: list = Field(
        default_factory=list, description="A list to track questions that have been completed."
    )

    def interpret_response(self, response: str):
        """
        Interpret and evaluate the candidate's response, and provide a score.
        """
        # Simulate interpretation and evaluation logic with scoring
        evaluation = random.choice(["Good", "Average", "Needs Improvement"])
        score = {"Good": 3, "Average": 2, "Needs Improvement": 1}[evaluation]
        
        question = self.questions[self.current_question_index]
        self.responses[question] = response
        self.feedback[question] = evaluation
        self.scores[question] = score
        
        return f"Response recorded. Evaluation: {evaluation} (Score: {score})"

    def provide_feedback(self):
        """
        Provide feedback based on the candidate's response.
        """
        current_question = self.questions[self.current_question_index]
        return f"Feedback for '{current_question}': {self.feedback[current_question]}"

    def adjust_questions(self):
        """
        Adjust the interview questions based on the candidate's performance.
        Adds a follow-up question if the response needs improvement.
        """
        current_question = self.questions[self.current_question_index]
        if self.feedback[current_question] == "Needs Improvement":
            additional_question = f"Can you provide more details on '{current_question}'?"
            self.questions.insert(self.current_question_index + 1, additional_question)
            return f"Adjusting questions. Next question: {additional_question}"
        return "No adjustment needed."

    def next_question(self):
        """
        Move to the next question in the list and mark the current question as completed.
        """
        current_question = self.questions[self.current_question_index]
        self.completed_questions.append(current_question)
        
        if self.current_question_index < len(self.questions) - 1:
            self.current_question_index += 1
            return f"Next question: {self.questions[self.current_question_index]}"
        else:
            return "All questions have been asked."

    def run(self, action: str, response: str = None):
        """
        Execute an action based on the command.
        
        Args:
            action (str): The action to perform (interpret, feedback, adjust, next).
            response (str, optional): The response from the candidate, required for 'interpret' action.
        
        Returns:
            str: The result of the action.
        """
        if action == "interpret":
            if response:
                return self.interpret_response(response)
            else:
                return "Response required for interpretation."
        elif action == "feedback":
            return self.provide_feedback()
        elif action == "adjust":
            return self.adjust_questions()
        elif action == "next":
            return self.next_question()
        else:
            return "Invalid action specified. Available actions: interpret, feedback, adjust, next."
