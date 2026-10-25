from langgraph.graph import StateGraph , START , END
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Sequence
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool 
from langchain_core.messages import BaseMessage,SystemMessage 
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-3.8-flash")

