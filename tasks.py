import os
from crewai import Task
from crewai_tools import tool


def writeToFile(result):
    with open("temp.md", "a") as file:
        file.write("\n")
        file.write(result.raw)


def Create_chapter(sequence, agent, context):
    return Task(
        description="Write a  chatper",
        expected_output=f"""Add a title of the new chatper and a block of text that is an additional chapter.
                        The title should be preceded by ## symbol for markdown purposes.
                        The title will be sequenced as ${sequence}. example for a title : Chapter 1: The rise of the champion.""",
        agent=agent,
        context=context,
        callback=writeToFile,
    )


def Suggest_topic(suggestor):
    file_names = os.listdir("./stories")
    for i in range(len(file_names)):
        file_names[i] = file_names[i].split(".")[0]
    blacklist = ",".join(file_names)
    expected_output = f"""A one setence topic describing the event by name and time.
                            The event should highlight an exceptional strategic shifting in human history.
                            The output should be used as a header for the story. So must be very concise. And preced by a #.
                            Also, avoid the following topics: {blacklist}"""
    return Task(
        description="Get suggestion about an interesting military event",
        expected_output=expected_output,
        agent=suggestor,
        callback=writeToFile,
    )


def Create_file_name(agent):
    return Task(
        description="You take a title of a story, and turn it into a filename in kebab case",
        expected_output="Kebab-case, up to 4-5 parts, based on the title you have been given. you will summarize the title and produce a kebab case.",
        agent=agent,
    )
