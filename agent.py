import asyncio
from llama_index.llms.google_genai import GoogleGenAI
from droidrun import DroidAgent, AdbTools

async def main():
    # load adb tools for the first connected device
    tools = await AdbTools.create()

    # Set up the Gemini LLM
    llm = GoogleGenAI(
        api_key="YOUR_API_KEY",  
        model="gemini-2.5-flash", 
    )

    # Create the DroidAgent
    agent = DroidAgent(
        goal='''Open ixigo train app
Find train from Rishikesh (YNRK) to New Delhi (NDLS)
Date after 23 Jan 2026 and before 26 Jan.
Select 3A, 3E or Sleeper Coach (Find cheapest option in these dates and coach).
Select Himanshu Haldar as Passenger. already saved in app.
NO insurance or any any offer.
Tick Consider Auto Upgradation 
Proceed to pay.
use UPI payment and enter UPI ID "XXXX-XXXX@XXX"
submit.''',
        llm=llm,
        tools=tools,
        vision=True,      # Set to True for vision models, False for text-only
        reasoning=False,  # Optional: enable planning/reasoning
    )

    # Run the agent
    result = await agent.run()
    print(f"Success: {result['success']}")
    if result.get('output'):
        print(f"Output: {result['output']}")

if __name__ == "__main__":
    asyncio.run(main())
