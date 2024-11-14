import unittest
from InterviewCoordinator.tools.CandidateInteractionTool import CandidateInteractionTool
from InterviewCoordinator.tools.CommunicationTool import CommunicationTool
from InterviewCoordinator.tools.InterviewFlowManagerTool import InterviewFlowManagerTool
from InterviewCoordinator.tools.GradioInterfaceTool import GradioInterfaceTool


class TestCandidateInteractionTool(unittest.TestCase):
    def test_welcome_message(self):
        tool = CandidateInteractionTool(
            candidate_name="John Doe",
            interview_structure="The interview has three stages: introduction, technical, and Q&A."
        )
        expected_output = (
            "Hello John Doe,\n\n"
            "Welcome to the interview process. We are excited to have you here today.\n\n"
            "Interview Structure:\n"
            "The interview has three stages: introduction, technical, and Q&A.\n\n"
            "Please feel free to ask any questions before we begin. We wish you the best of luck!"
        )
        self.assertEqual(tool.run(), expected_output)



class TestCommunicationTool(unittest.TestCase):
    def test_send_and_receive_message(self):
        tool = CommunicationTool(
            message_to_send="Please provide the candidate's evaluation report."
        )
        tool.send_message("EvaluationAgent")
        self.assertEqual(tool.received_message, "Message sent to EvaluationAgent: Please provide the candidate's evaluation report.")
        
        tool.receive_message("KnowledgeRetrievalAgent")
        self.assertEqual(tool.received_message, "Message received from KnowledgeRetrievalAgent: [Simulated message content]")

    def test_run_communication(self):
        tool = CommunicationTool(
            message_to_send="Please provide the candidate's evaluation report."
        )
        result = tool.run()
        self.assertEqual(result, "Communication between agents completed successfully")



class TestGradioInterfaceTool(unittest.TestCase):
    def test_gradio_interface_launch(self):
        tool = GradioInterfaceTool(
            question="Describe a challenging problem you solved.",
            instructions="Answer in detail."
        )
        result = tool.run()
        self.assertEqual(result, "Gradio interface launched successfully")



class TestInterviewFlowManagerTool(unittest.TestCase):
    def test_interview_flow_with_follow_ups(self):
        tool = InterviewFlowManagerTool(
            initial_question="What is your experience with Python?",
            follow_up_questions={
                "beginner": "Can you describe a simple project you've worked on?",
                "intermediate": "What libraries do you frequently use?",
                "advanced": "Have you contributed to any open-source projects?"
            }
        )


# Run the tests
if __name__ == "__main__":
    unittest.main()
