class JobFinder(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Job Finder",
            role="Finds relevant jobs based on criteria",
            goal="Scrape job listings matching user preferences",
            backstory="An AI agent specialized in job searches",
        )
    def execute(self, criteria):
        from utils.logger import scrape_jobs
        return scrape_jobs(criteria)