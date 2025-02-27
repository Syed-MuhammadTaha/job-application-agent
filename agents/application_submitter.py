from agents.base_agent import BaseAgent
class ApplicationSubmitter(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Application Submitter",
            role="Fills and submits job applications",
            goal="Automate job application process",
            backstory="AI agent trained to fill job forms",
        )
    def execute(self, job):
        from utils.submitter import submit_application
        return submit_application(job)