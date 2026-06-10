from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
llm=ChatOllama(model="llama3")
template=PromptTemplate(
    input_variables=["question"],
    template="""
    You are a teacher.
Rules:
- give ans in json format
- make the ans simple
-1 line ans
- Do NOT write anything outside JSON
- Do NOT add extra text like "Here is the answer"
format:{{
"defination":"",
"example":""
}}
Question:{question}

"""
)
while True:
    question=input("Enter your question:")
    if question.lower() in ["exit", "quit"]:
        print("Exiting the program.")
        break
    response = llm.invoke(template.format(question=question)) 
    print("Answer:", response.content)