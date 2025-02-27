from agents.base_agent import BaseAgent
class ResumeUpdater(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Resume Updater",
            role="Updates resume to match job descriptions",
            goal="Tailor resumes for better job fit",
            backstory="AI agent specializing in resume optimization",
        )
    def execute(self, resume, job_description):
        from utils.resume_optimizer import update_resume
        return update_resume(resume, job_description)