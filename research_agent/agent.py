from google.adk.agents import Agent

root_agent = Agent(
    name="document_outliner_agent",
    model="gemini-2.5-pro",
    description=(
        "Agent to create a document outline and generate keyframes for a short video, "
        "with a specific personal focus, based on input documents and user persona."
    ),
    instruction=(
        "You are an agent that receives input documents (like regulations or articles) "
        "and user profile information (like a CV or LinkedIn profile). "
        "Your tasks are to: "
        "1. Generate a structured outline of the document, highlighting aspects relevant to the user's persona. "
        "2. Generate keyframes for a short video explaining the document in a highly personal style, tailored to the user's persona."
    ),
    tools=[],
)