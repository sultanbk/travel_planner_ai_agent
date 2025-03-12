from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.tools import BaseTool
from dotenv import load_dotenv
from crewai_tools import (
    SerperDevTool,
    ScrapeWebsiteTool,
)

load_dotenv()

@CrewBase
class TravelPlanner():
    # Initialize tools
    search_tool = SerperDevTool()
    scrape_tool = ScrapeWebsiteTool()

    """TravelPlanner crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def iternary_planner(self) -> Agent:
        return Agent(
            config=self.agents_config['iternary_planner'],
            verbose=True,
            tools=[self.search_tool, self.scrape_tool],
        )

    @agent
    def transportation(self) -> Agent:
        return Agent(
            config=self.agents_config['transportation'],
            verbose=True,
            tools=[self.search_tool],
        )

    @agent
    def accommodation(self) -> Agent:
        return Agent(
            config=self.agents_config['accommodation'],
            verbose=True,
            tools=[self.search_tool],
        )

    @agent
    def weather(self) -> Agent:
        return Agent(
            config=self.agents_config['weather'],
            verbose=True,
            tools=[self.search_tool],
        )

    @task
    def iternary_planner_task(self) -> Task:
        return Task(
            config=self.tasks_config['iternary_planner_task'],
            agent=self.iternary_planner(),
        )

    # @task
    # def destination_suggestion_task(self) -> Task:
    #     return Task(
    #         config=self.tasks_config['destination_suggestion_task'],
    #         agent=self.iternary_planner(),
    #     )

    @task
    def best_travel_routes_task(self) -> Task:
        return Task(
            config=self.tasks_config['best_travel_routes_task'],
            agent=self.transportation(),
            output_file='transportation_report.md',
        )

    @task
    def accommodation_task(self) -> Task:
        return Task(
            config=self.tasks_config['accommodation_task'],
            agent=self.accommodation(),
            output_file='accommodation_report.md',
        )

    @task
    def weather_task(self) -> Task:
        return Task(
            config=self.tasks_config['weather_task'],
            agent=self.weather(),
            output_file='weather_report.md',
        )

    @crew
    def crew(self) -> Crew:
        """Creates the TravelPlanner crew"""
        return Crew(
            agents=[self.iternary_planner(), self.transportation(), self.accommodation(), self.weather()],
            # agents=[self.iternary_planner()],
            
            tasks=[
                self.iternary_planner_task(),
                # self.destination_suggestion_task(),
                self.best_travel_routes_task(),
                self.accommodation_task(),
                self.weather_task(),
            ],
            process=Process.sequential,
            verbose=True,
        )