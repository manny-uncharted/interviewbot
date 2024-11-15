from agency_swarm.tools import BaseTool
from pydantic import Field
from typing import Optional

class CommunicationTool(BaseTool):
    """
    This tool facilitates communication with other agents like the EvaluationAgent and KnowledgeRetrievalAgent.
    It can send and receive messages, ensuring smooth collaboration between agents during the interview process.
    """

    message_to_send: str = Field(
        ..., description="The message to be sent to another agent."
    )
    received_message: Optional[str] = Field(
        None, description="The message received from another agent."
    )

    # Simulated message store for inter-agent communication
    message_store = {}

    def send_message(self, recipient_agent: str):
        """
        Sends a message to the specified recipient agent.
        
        Args:
            recipient_agent (str): The name of the agent to send the message to.
            
        Returns:
            str: Confirmation that the message has been sent.
        """
        # Store the message in the shared message store
        CommunicationTool.message_store[recipient_agent] = self.message_to_send
        return f"Message sent to {recipient_agent}: {self.message_to_send}"

    def receive_message(self, sender_agent: str):
        """
        Receives a message from the specified sender agent.
        
        Args:
            sender_agent (str): The name of the agent from whom to receive the message.
        
        Returns:
            str: The received message content, or an indication if no message is available.
        """
        if sender_agent in CommunicationTool.message_store:
            self.received_message = CommunicationTool.message_store.pop(sender_agent)
            return f"Message received from {sender_agent}: {self.received_message}"
        else:
            return f"No new message from {sender_agent}."

    def run(self, action: str, agent_name: str):
        """
        Executes a communication action, either sending or receiving a message, based on the specified action.
        
        Args:
            action (str): Action to perform, either 'send' or 'receive'.
            agent_name (str): Name of the agent to send to or receive from.
        
        Returns:
            str: The result of the send or receive action.
        """
        if action == "send":
            return self.send_message(agent_name)
        elif action == "receive":
            return self.receive_message(agent_name)
        else:
            return "Invalid action. Please specify 'send' or 'receive'."
