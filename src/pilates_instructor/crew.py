from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class PilatesInstructor():
    """PilatesInstructor crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def pilates_researcher(self) -> Agent:
        return Agent(config=self.agents_config['pilates_researcher'], verbose=True)


    @agent
    def workout_planner(self) -> Agent:
        return Agent(config=self.agents_config['workout_planner'], verbose=True)

    @agent
    def pilates_instructor(self) -> Agent:
        return Agent(config=self.agents_config['pilates_instructor'], verbose=True)

    @task
    def research_workout_task(self) -> Task:
        return Task(config=self.tasks_config['research_workout_task'])

    @task
    def generate_audio_script_task(self) -> Task:
        return Task(config=self.tasks_config['generate_audio_script_task'], output_file='script.md')

    @crew
    def crew(self) -> Crew:
        """Creates the PilatesInstructor crew"""

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
