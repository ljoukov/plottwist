
import asyncio
import os
from google.adk.agents import Agent
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types

# Assuming agent definition is in agent.py
from .agent import root_agent

# --- Configuration ---
# Replace with your actual API key or use environment variables
# os.environ["GOOGLE_API_KEY"] = "YOUR_GOOGLE_API_KEY"
# os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "False" # Use API key directly

APP_NAME = "research_agent_app"
USER_ID = "user_test"
SESSION_ID = "session_test_001"

async def call_agent_async(runner: Runner, query: str):
    """Sends a query to the agent and prints the final response."""
    print(f"\n>>> User Query: {query}")

    content = types.Content(role='user', parts=[types.Part(text=query)])
    final_response_text = "Agent did not produce a final response."

    async for event in runner.run_async(user_id=USER_ID, session_id=SESSION_ID, new_message=content):
        if event.is_final_response():
            if event.content and event.content.parts:
                final_response_text = event.content.parts[0].text
            elif event.actions and event.actions.escalate:
                final_response_text = f"Agent escalated: {event.error_message or 'No specific message.'}"
            break

    print(f"<<< Agent Response: {final_response_text}")

async def main():
    # --- Setup ---
    if not os.environ.get("GOOGLE_API_KEY"):
        print("Error: GOOGLE_API_KEY environment variable not set.")
        return

    session_service = InMemorySessionService()
    session = session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID
    )
    print(f"Session created: App='{APP_NAME}', User='{USER_ID}', Session='{SESSION_ID}'")

    runner = Runner(
        agent=root_agent,
        app_name=APP_NAME,
        session_service=session_service
    )
    print(f"Runner created for agent '{runner.agent.name}'.")

    # --- Interaction ---
    await call_agent_async(runner, "What time is it in New York?")
    await call_agent_async(runner, "What's the weather like there?")
    await call_agent_async(runner, "What about the weather in London?") # Expect tool error

if __name__ == "__main__":
    # Use asyncio.run() to execute the async main function
    try:
        asyncio.run(main())
    except RuntimeError as e:
        # Handle potential issues if running in an environment like Jupyter
        # where an event loop might already be running.
        if "Cannot run the event loop while another loop is running" in str(e):
            print("Detected running event loop. Attempting to run main() in the existing loop.")
            # This approach might be needed in some environments like notebooks
            loop = asyncio.get_event_loop()
            loop.run_until_complete(main())
        else:
            raise e
