* ### InterviewBot Agency Manifesto

  #### Mission:

  To streamline and elevate the technical interview process by leveraging an AI-powered multi-agent system. Using Agency Swarm, the InterviewBot will conduct interactive, adaptive technical interviews with developer candidates, providing real-time assessment and feedback based on predefined criteria. This approach enables efficient, data-driven evaluations of candidate skills and knowledge.

  #### Goals:


  * Conduct seamless technical interviews, including assessments in Python programming, APIs, cloud, containerization, and the Agency Swarm framework.
  * Reference relevant documentation to support interview questions and clarify technical concepts on request.
  * Automate candidate assessment by recording and scoring responses to predefined questions and saving the results for further review.
  * Facilitate an interactive interview experience using Gradio UI for straightforward candidate interaction.

  ---

  ### Agency Structure

  1. **InterviewCoordinator (Primary Agent)**
     * **Role** : Manages the overall interview flow and candidate interactions.
     * **Responsibilities** :
     * Greet and introduce the candidate to the interview format.
     * Control the sequence of questions and phases (technical questions, scenario-based questions).
       * Technical questions covering:
         * Python programming and APIs.
         * OpenAI's Chat Completion API and Assistants API.
         * Vector databases and embeddings.
         * Containerization (Docker), GitHub Workflows, GCP/AWS (optional).
         * Agency Swarm framework knowledge.
       * Scenario-based questions to assess problem-solving abilities.
     * Adapt questions based on candidate responses and progress through different interview sections.
     * Summarize the interview outcome and provide closing remarks.
     * **Skills Required** :
     * State management for tracking phases and question flow.
     * Question adaptation based on candidate responses.
     * Coordination with the Knowledge Retrieval Agent for supporting information.
  2. **EvaluationAgent (Supporting Agent)**
     * **Role** : Evaluates and scores candidate responses in real-time based on expected criteria.
     * **Responsibilities** :
     * Analyze each response for relevance, accuracy, and completeness using an llm and the candidate criteria sheet.
     * Score responses based on predefined criteria (stored in a Candidate Criteria Sheet.xlsx) provided.
     * Store scores and feedback in a structured JSON file for each candidate, with their names.
     * **Skills Required** :
     * Text analysis and scoring logic.
     * Response logging and file management for structured storage.
     * Communication with InterviewCoordinator to confirm scores and log results.
  3. **KnowledgeRetrievalAgent (Supporting Agent)**
     * **Role** : Retrieves relevant information from the knowledge base which is a pinecone vector database to assist with context-specific questions, to populate the database using txt files and urls provided to load information into the database.
     * These are the links you can scrape to populate the knowledge based:
       * [https://platform.openai.com/docs/assistants/overview](https://platform.openai.com/docs/assistants/overview)
       * [https://platform.openai.com/docs/guides/text-generation](https://platform.openai.com/docs/guides/text-generation)
     * **Responsibilities** :
     * Parse and index documents provided (e.g., Agency Swarm documentation, OpenAI APIs, Candidate Criteria).
     * Handle requests for clarifications or topic-specific information based on candidate inquiries.
     * Dynamically supply the InterviewCoordinator with pertinent information for deeper interview questions.
     * **Skills Required** :
     * Document indexing and search capabilities (RAG - Retrieval Augmented Generation).
     * Query processing based on keywords/topics from InterviewCoordinator.
     * Adaptability to update knowledge base as required.

  ---

  ### Communication Flows

  The **sequential and responsive flow** facilitates a smooth and adaptive interview process:

  * The **InterviewCoordinator** starts with the introduction and initiates technical questions.
  * **EvaluationAgent** assesses responses and sends scores back to InterviewCoordinator.
  * **KnowledgeRetrievalAgent** dynamically supplies context when InterviewCoordinator encounters topics that require detailed clarification, enhancing the interview experience for complex questions.
  * This flow ensures each agent remains focused on its specialized role while contributing to a seamless candidate experience.

  ---

  ### Tools and APIs

  1. **InterviewCoordinator** :

  * **Tools** : Gradio UI (Frontend Interface).
  * **APIs** : Communication with EvaluationAgent and KnowledgeRetrievalAgent.

  1. **EvaluationAgent** :

  * **Tools** : Text analysis libraries (e.g., NLTK or SpaCy) for keyword matching.
  * **Storage** : JSON logging for candidate responses and scores.

  1. **KnowledgeRetrievalAgent** :

  * **Tools** : Simple RAG system, potentially with Faiss or another vector database for document indexing and retrieval.
  * **APIs** : OpenAI Chat Completion API for advanced responses or generating clarifications when additional knowledge retrieval is needed.
  * **Storage** : Indexed versions of the knowledge base documents (Agency Swarm documentation, OpenAI APIs, Candidate Criteria).

  ---

  ### Development and Implementation Outline

  1. **Agent Development** :

  * **Instructions** (`instructions.md`): Define a clear interview workflow for InterviewCoordinator.
  * **Phases** : Set phases for each interview section—technical questions, scenario-based questions, and closing.
  * **Question and Answer Logic** : Include sample questions, keywords, and criteria for EvaluationAgent’s scoring reference.
  * **Document Parsing** : Load and index knowledge base documents for KnowledgeRetrievalAgent.

  1. **Testing and Quality Assurance** :

  * Write unit tests to verify agent-specific functions, including response scoring, knowledge retrieval, and state transitions.
  * Conduct mock interviews to evaluate performance under various scenarios.

  1. **Deployment** :

  * **Containerize** the entire application using Docker to ensure seamless deployment with `docker-compose up`.
  * **Documentation** : Provide a detailed README with setup, deployment, and usage instructions.
