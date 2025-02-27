from crewai import Task
class MatchResume(Task):
    def __init__(self, matcher, jobs, resume):
        super().__init__(
            description="Match resume with job descriptions",
            agent=matcher,
            expected_output="Ranked job list based on resume fit",
        )
        self.jobs = jobs
        self.resume = resume
    def run(self):
        return self.agent.execute(self.jobs, self.resume)
