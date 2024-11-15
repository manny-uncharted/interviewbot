from agency_swarm.tools import BaseTool
from pydantic import Field

class ConversationManager(BaseTool):
    """
    A tool to manage the flow of conversation during technical interviews.
    It can start, pause, and resume interviews, and track the progress to ensure all necessary topics are covered.
    """

    topics: list = Field(
        ..., description="A list of topics that need to be covered during the interview."
    )
    current_topic_index: int = Field(
        0, description="The index of the current topic being discussed."
    )
    is_paused: bool = Field(
        False, description="A flag indicating whether the interview is currently paused."
    )
    completed_topics: list = Field(
        default_factory=list, description="A list of completed topics for reference."
    )

    def start_interview(self):
        """
        Start the interview by setting the current topic index to 0 and ensuring the interview is not paused.
        """
        if not self.topics:
            return "No topics available to cover in this interview."
        
        self.current_topic_index = 0
        self.is_paused = False
        self.completed_topics.clear()  # Clear completed topics at the start
        return f"Interview started. Current topic: {self.topics[self.current_topic_index]}"

    def pause_interview(self):
        """
        Pause the interview by setting the is_paused flag to True.
        """
        self.is_paused = True
        return "Interview paused."

    def resume_interview(self):
        """
        Resume the interview by setting the is_paused flag to False.
        """
        if self.is_paused:
            self.is_paused = False
            return f"Interview resumed. Current topic: {self.topics[self.current_topic_index]}"
        else:
            return "Interview is already in progress."

    def next_topic(self):
        """
        Move to the next topic in the list if the interview is not paused.
        """
        if not self.is_paused:
            if self.current_topic_index < len(self.topics) - 1:
                self.completed_topics.append(self.topics[self.current_topic_index])
                self.current_topic_index += 1
                return f"Moving to next topic: {self.topics[self.current_topic_index]}"
            else:
                return "All topics have been covered."
        else:
            return "Cannot move to the next topic while the interview is paused."

    def previous_topic(self):
        """
        Move back to the previous topic in the list if possible and if the interview is not paused.
        """
        if not self.is_paused:
            if self.current_topic_index > 0:
                self.current_topic_index -= 1
                return f"Returning to previous topic: {self.topics[self.current_topic_index]}"
            else:
                return "Already at the first topic."
        else:
            return "Cannot go to the previous topic while the interview is paused."

    def restart_interview(self):
        """
        Restart the interview by resetting the current topic index to 0 and clearing completed topics.
        """
        self.current_topic_index = 0
        self.completed_topics.clear()
        self.is_paused = False
        return f"Interview restarted. Current topic: {self.topics[self.current_topic_index]}"

    def run(self, action: str):
        """
        Run method to handle general actions. 
        It accepts an action as input and maps it to the relevant method.
        """
        actions = {
            "start": self.start_interview,
            "pause": self.pause_interview,
            "resume": self.resume_interview,
            "next": self.next_topic,
            "previous": self.previous_topic,
            "restart": self.restart_interview
        }
        
        if action in actions:
            return actions[action]()
        else:
            return "Invalid action specified."
