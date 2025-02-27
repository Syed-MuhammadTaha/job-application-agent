from agents.base_agent import BaseAgent
class ResumeMatcher(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Resume Matcher",
            role="Matches resume with job descriptions",
            goal="Analyze job postings and rank them by fit",
            backstory="Expert in NLP for job relevance scoring",
        )
    def execute(self, jobs, resume):
        from utils.resume_optimizer import parse_resume
        from utils.matcher import match_resume
        resume_text = parse_resume(resume)
        return match_resume(jobs, resume_text)