from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0.9)

response = llm.invoke("Why do parrots talk?")
print(response)