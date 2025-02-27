from crewai import Task
class UpdateResume(Task):
    def __init__(self, updater, resume, job_description):
        super().__init__(
            description="Update resume to match job description",
            agent=updater,
            expected_output="Updated resume tailored for job",
        )
        self.resume = resume
        self.job_description = job_description
    def run(self):
        return self.agent.execute(self.resume, self.job_description)