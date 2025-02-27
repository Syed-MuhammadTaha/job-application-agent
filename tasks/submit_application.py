from crewai import Task
class SubmitApplication(Task):
    def __init__(self, submitter, job):
        super().__init__(
            description="Submit job applications",
            agent=submitter,
            expected_output="Confirmation of submitted applications",
        )
        self.job = job
    def run(self):
        return self.agent.execute(self.job)