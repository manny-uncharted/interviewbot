from agency_swarm.tools import BaseTool
from pydantic import Field
import gradio as gr

class GradioInterfaceTool(BaseTool):
    """
    This tool handles the Gradio UI for the frontend interface, allowing the InterviewCoordinator agent
    to interact with candidates. It displays questions, receives candidate responses, and shows any
    necessary instructions or information during the interview process.
    """

    question: str = Field(
        ..., description="The question to be displayed to the candidate."
    )
    instructions: str = Field(
        "", description="Any additional instructions or information to be shown to the candidate."
    )

    def run(self):
        """
        Sets up a Gradio interface to display the question and instructions and to receive the candidate's response.
        """
        def respond(answer):
            # Placeholder response logic; can be modified as needed
            # return f"Received response: {answer}"
            return gr.ChatMessage(role='user', content=answer)

        with gr.Blocks() as demo:
            gr.Markdown(f"### Instructions\n{self.instructions}")
            gr.Markdown(f"**Question:** {self.question}")
            response = gr.Textbox(label="Your Response", placeholder="Type your response here...")
            output = gr.Textbox(label="System Response")
            submit = gr.Button("Submit")
            submit.click(fn=respond, inputs=response, outputs=output)

        demo.launch()

        return "Gradio interface launched successfully"

