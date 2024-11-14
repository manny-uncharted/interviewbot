from agency_swarm import Agency, set_openai_key
from KnowledgeRetrievalAgent import KnowledgeRetrievalAgent
from KnowledgeRetrievalAgent import KnowledgeRetrievalAgent
from EvaluationAgent import EvaluationAgent
from InterviewCoordinator import InterviewCoordinator

from utils.constants import OPENAI_API_KEY

set_openai_key(key=OPENAI_API_KEY)

interview_coordinator = InterviewCoordinator()                                                                 
evaluation_agent = EvaluationAgent()                                                                           
knowledge_retrieval_agent = KnowledgeRetrievalAgent() 

agency = Agency([
    interview_coordinator,  # Entry point for communication with the user                                      
    [interview_coordinator, evaluation_agent],  # Communication between InterviewCoordinator and EvaluationAge 
    [interview_coordinator, knowledge_retrieval_agent],  # Communication between InterviewCoordinator and     KnowledgeRetrievalAgent                                                                                   
    [evaluation_agent, knowledge_retrieval_agent]  # Communication between EvaluationAgent and               KnowledgeRetrievalAgent
],
shared_instructions='./agency_manifesto.md',
max_prompt_tokens=25000,
temperature=0.3)

                
if __name__ == '__main__':
    agency.demo_gradio()
