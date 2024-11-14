from agency_swarm.tools import BaseTool
from pydantic import Field

class CommunicationTool(BaseTool):
    """
    This tool facilitates communication with the EvaluationAgent and KnowledgeRetrievalAgent.
    It can send and receive messages, ensuring smooth collaboration between agents during the interview process.
    """

    message_to_send: str = Field(
        ..., description="The message to be sent to another agent."
    )
    received_message: str = Field(
        None, description="The message received from another agent."
    )

    def send_message(self, recipient_agent):
        """
        Sends a message to the specified recipient agent.
        """
        # Implement sending message logic here, such as using a messaging system
        # Placeholder for actual messaging code
        self.received_message = f"Message sent to {recipient_agent}: {self.message_to_send}"
        print(self.received_message)

    def receive_message(self, sender_agent):
        """
        Receives a message from the specified sender agent.
        """
        # Simulate receiving a message from sender agent
        self.received_message = f"Message received from {sender_agent}: [Simulated message content]"
        print(self.received_message)

    def run(self):
        """
        Demonstrates sending and receiving messages between agents.
        """
        self.send_message("EvaluationAgent")
        self.receive_message("KnowledgeRetrievalAgent")
        return "Communication between agents completed successfully"


