# InterviewBot

InterviewBot is a deployable AI-powered interview chatbot built with the Agency Swarm framework. This chatbot conducts technical interviews, leveraging a multi-agent system to interact with candidates, evaluate their responses, and provide feedback in real time. The chatbot references relevant documentation to ask questions and clarify complex concepts, ensuring a comprehensive interview process.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Prerequisites](#prerequisites)
3. [Setup and Installation](#setup-and-installation)
4. [Usage](#usage)
5. [Deployment with Docker Compose](#deployment-with-docker-compose)
6. [Troubleshooting](#troubleshooting)
7. [Project Structure](#project-structure)

---

## Project Overview

InterviewBot uses three primary agents:

1. **InterviewCoordinator** - Manages the interview flow and coordinates candidate interactions.
2. **EvaluationAgent** - Evaluates candidate responses based on predefined criteria.
3. **KnowledgeRetrievalAgent** - Dynamically retrieves information from a knowledge base to support questions and clarifications.

The frontend is powered by Gradio UI for an interactive and user-friendly experience.

---

## Prerequisites

* Python 3.10 or above
* Docker & Docker Compose (for containerized deployment)
* OpenAI API key (for accessing the Chat Completion API)

---

## Setup and Installation

1. **Clone the repository:**

   ```
   cd InterviewBot
   ```
2. **Install dependencies:**
   Use `requirements.txt` to install the necessary Python packages:

   ```
   pip install -r requirements.txt
   ```
3. **Set up environment variables:**
   To access the OpenAI API, you need an API key. Create an `.env` file in the root directory and add the following line:

   ```
   OPENAI_API_KEY=your_openai_api_key_here
   PINECONE_API_KEY=
   ```
4. **Run Locally:**
   Use the following command to start the interview bot locally:

   ```
   python agency.py
   ```

   The bot will be accessible through the Gradio interface in your browser at `http://localhost:7860`.

---

## Usage

1. **Starting the Interview:**
   Once you access the Gradio UI, follow the prompts to begin the interview. The InterviewCoordinator agent will guide you through the interview process.
2. **Responding to Questions:**
   Answer the questions as they appear. The EvaluationAgent will score each response, while the KnowledgeRetrievalAgent can provide additional information on request.
3. **Completing the Interview:**
   At the end of the interview, your results will be saved in a JSON file with a timestamp, accessible in the `storage/candidates/` directory.

---

## Deployment with Docker Compose

For ease of deployment, InterviewBot is containerized with Docker.

1. **Build and Run with Docker Compose:**
   From the root directory, use Docker Compose to build and start the container:
   ```
   docker-compose up --build
   ```
2. **Access the InterviewBot:**
   Once the container is running, access the Gradio UI in your browser at `http://localhost:7860`.
3. **Stop the Container:**
   To stop the Docker container, press `CTRL+C` in the terminal where Docker is running or use:
   ```
   docker-compose down
   ```

---

## Troubleshooting

* **Gradio UI Not Loading** :
* Check if the server is running on `http://localhost:7860`. If you’re unable to access it, ensure there are no port conflicts.
* If you are running multiple instances, stop previous containers by running `docker-compose down`.
* **OpenAI API Key Issues** :
* If there are errors related to the OpenAI API, confirm your API key in the `.env` file and verify that it’s correctly set.
* **Docker Build Issues** :
* Ensure Docker is installed and running. If the build fails, try clearing Docker cache:
  ```
  docker-compose down --rmi all
  docker-compose up --build
  ```
* **Agent Errors** :
* If agents are not responding as expected, ensure `requirements.txt` dependencies are installed. Restart the application with `python agency.py` or `docker-compose up --build` if needed.

---

## Project Structure

```
│
├── agent/
│   ├── init.py             # Agent package
│   ├── interview_agent.py       # Interview Coordinator logic
│   ├── evaluation_agent.py      # Evaluation agent logic
│   ├── retrieval_agent.py       # Knowledge Retrieval agent logic
│
├── knowledge_base/              # Knowledge base files
│   ├── cursorrules.txt
│   ├── assistants_api_overview.txt
│   ├── chat_completions_api.txt
│   ├── candidate_criteria_sheet.xlsx
│
├── storage/
│   └── candidates/              # Stores candidate JSON response files
│
├── Dockerfile                   # Docker setup file
├── docker-compose.yml           # Docker Compose setup file
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
└── agency.py                    # Main entry point for running the bot locally
```
