import typer
from typing import Optional, List
from phi.agent import Agent
from phi.knowledge.pdf import PDFUrlKnowledgeBase
from phi.vectordb.pgvector import PgVector2
from phi.storage.agent.postgres import PgAgentStorage
from phi.model.groq import Groq  # model

import os
from dotenv import load_dotenv

load_dotenv()


os.environ["GROQ_API_KEY"] = os.environ["GROQ_API_KEY"]
db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=PgVector2(collection="recipes", db_url=db_url),
)

knowledge_base.load()


storage = PgAgentStorage(table_name="pdf_assistant", db_url=db_url)


agent = Agent(
    model=Groq(id="llama3-8b-8192"),
    knowledge=knowledge_base,
    # Add a tool to read chat history.
    read_chat_history=True,
    show_tool_calls=True,
    markdown=True,
    search_knowledge=True,
    # debug_mode=True,
)
# agent.cli_app(markdown=True)

agent.print_response("How do I make chicken and galangal in coconut milk soup")
agent.print_response("What was my last question?")


# if __name__ == "__main__":
#     typer.run()
