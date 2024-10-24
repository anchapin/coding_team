from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
# from coding_team.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class CodingTeamCrew():
	"""CodingTeam crew"""

	@agent
	def manager(self) -> Agent:
		return Agent(
			config=self.agents_config['manager'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True
		)

	@agent
	def junior_developer(self) -> Agent:
		return Agent(
			config=self.agents_config['junior_developer'],
			verbose=True
		)

	@agent
	def senior_developer(self) -> Agent:
		return Agent(
			config=self.agents_config['senior_developer'],
			verbose=True
		)

	@agent
	def document_manager(self) -> Agent:
		return Agent(
			config=self.agents_config['document_manager'],
			verbose=True
		)

	@task
	def manager_task(self) -> Task:
		return Task(
			config=self.tasks_config['manager_task'],
		)

	@task
	def junior_developer_task(self) -> Task:
		return Task(
			config=self.tasks_config['junior_developer_task'],
			output_file='report.md'
		)

	@task
	def senior_developer_task(self) -> Task:
		return Task(
			config=self.tasks_config['senior_developer_task'],
			output_file='report.md'
		)

	@task
	def document_manager_task(self) -> Task:
		return Task(
			config=self.tasks_config['document_manager_task'],
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the CodingTeam crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)