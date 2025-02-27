from crewai import Task
class FindJobs(Task):
    def __init__(self, job_finder, criteria):
        super().__init__(
            description="Find jobs based on user preferences",
            agent=job_finder,
            expected_output="A list of job descriptions",
        )
        self.criteria = criteria
    def run(self):
        return self.agent.execute(self.criteria)
