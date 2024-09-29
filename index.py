import os
from dotenv import load_dotenv
from crewai import Agent,Crew,Task,Process
from tasks import Create_chapter


os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_SECRET')

suggestor = Agent(
    role="The ideas person",
    goal="Discover a unique and intereting topic for a story happened any time in the past. Involving war and tactics",
    backstory="""You are a curious person who wants to learn about the world,
                 from every time in the world. You wish to uncover unique subjcets""",
    verbose=True
)

writer=Agent(
    role="The writer of the story",
    goal="""You will add another chapter to a story each time you are referred to.""",
    backstory="""Your writing should be entertining.
            Your writing should be easy to digest. You favor drama and and strategic in a high level    .
            The english should be dead-simple.
            Each one of your chapters are rather short. 4-5 sentences typically.
              """,
    verbose=True
)

suggest_topic = Task(
    description="Get suggestion about an interesting military event",
    expected_output="""A one setence topic describing the event by name and time.
                        The event should highlight an exceptional strategic shifting in human history.
                        The output should be used as a header for the story. So must be very concise.""",
    agent=suggestor
)

task_1 = Create_chapter(1,writer,[])
task_2 = Create_chapter(2,writer,[task_1])
task_3 = Create_chapter(3,writer,[task_1,task_2])
task_4 = Create_chapter(    4,writer,[task_1,task_2,task_3])

crew = Crew(
    agents=[suggestor],
    tasks=[suggest_topic, task_1,task_2,task_3,task_4],
    verbose=True,
    process = Process.sequential
)

result = crew.kickoff()

print("START")