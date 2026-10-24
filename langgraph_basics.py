from typing import TypedDict,Dict
from langgraph.graph import StateGraph, START,END




class MsgState(TypedDict):
    message:str


def greeting_node(state: MsgState) -> MsgState:
    """simple node that adds greeting message to the state"""
    state['message'] = "hello " + state["message"] + " Welcome to LangGraph"
    return state


graph= StateGraph(MsgState)
graph.add_node("initial",greeting_node)

graph.add_edge(START,"initial")
graph.add_edge("initial",END)

bot=graph.compile()
# print(bot)

reponse = bot.invoke({"message":"cs_zone.it"})

print(reponse)
