from crewai import Task
class LogApplication(Task):
    def __init__(self, logger, job, status):
        super().__init__(
            description="Log applied jobs into a record",
            agent=logger,
            expected_output="Job application logged successfully",
        )
        self.job = job
        self.status = status
    def run(self):
        return self.agent.execute(self.job, self.status)