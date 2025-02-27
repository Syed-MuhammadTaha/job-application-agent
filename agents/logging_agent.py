from agents.base_agent import BaseAgent
class LoggingAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Logging Agent",
            role="Logs job application details",
            goal="Maintain a record of all job applications",
            backstory="AI agent responsible for logging applications",
        )
    def execute(self, job, status):
        from utils.logger import log_application
        return log_application(job, status)
