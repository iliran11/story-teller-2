from crewai import Task
from crewai_tools import FileWriterTool

def writeToFile(result):
    with open("example.md", "a") as file:
        file.write("\n")
        file.write(result.raw)

def Create_chapter(sequence,agent,context):  
    return Task(
        description="Write a  chatper",
    expected_output=f"""Add a title of the new chatper and a block of text that is an additional chapter.
                        The title should be preceded by ## symbol for markdown purposes.
                        The title will be sequenced as ${sequence}. example for a title : Chapter 1: The rise of the champion.""",
    agent=agent,
    context=context,
    callback=writeToFile
)

suggest_topic = Task(
    description="Get suggestion about an interesting military event",
    expected_output="""A one setence topic describing the event by name and time.
                        The event should highlight an exceptional strategic shifting in human history.
                        The output should be used as a header for the story. So must be very concise.""",
    agent=suggestor
)