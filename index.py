import os
import shutil
from dotenv import load_dotenv
from crewai import Agent, Crew, Task, Process
from tasks import Create_chapter, Suggest_topic, Create_file_name

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_SECRET")


with open('./temp.md', 'w'):
    pass  # Do nothing, just create or truncate the file

suggestor = Agent(
    role="The ideas person",
    goal="Discover a unique and intereting topic for a story happened any time in the past. Involving war and tactics",
    backstory="""You are a curious person who wants to learn about the world,
                 from every time in the world. You wish to uncover unique subjcets""",
    verbose=True,
)

file_name_creator = Agent(
    role="Just to create the filename string that will be the story",
    goal="Create a recognizable filename",
    backstory="you are good at summarizing things",
    verbose=True,
)

writer = Agent(
    role="The writer of the story",
    goal="""You will add another chapter to a story each time you are referred to.""",
    backstory="""Your writing should be entertining.
            Your writing should be easy to digest. You favor drama and and strategic in a high level    .
            The english should be dead-simple.
            Each one of your chapters are rather short. 4-5 sentences typically.
              """,
    verbose=True,
)

task_suggest_topic = Suggest_topic(suggestor)
task_create_filename = Create_file_name(file_name_creator)
task_1 = Create_chapter(1, writer, [])
task_2 = Create_chapter(2, writer, [task_1])
task_3 = Create_chapter(3, writer, [task_1, task_2])
task_4 = Create_chapter(4, writer, [task_1, task_2, task_3])

crew = Crew(
    agents=[suggestor, writer],
    tasks=[task_suggest_topic, task_create_filename, task_1, task_2, task_3, task_4],
    verbose=True,
    process=Process.sequential,
)

result = crew.kickoff()
shutil.move("./temp.md", f"""./stories/{task_create_filename.output.raw}.md""")
print("START")
