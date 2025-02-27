from agents.job_finder import JobFinder
from agents.resume_matcher import ResumeMatcher
from agents.application_submitter import ApplicationSubmitter
from agents.resume_updater import ResumeUpdater
from agents.logging_agent import LoggingAgent
from tasks.find_jobs import FindJobs
from tasks.match_resume import MatchResume
from tasks.update_resume import UpdateResume
from tasks.submit_application import SubmitApplication
from tasks.log_application import LogApplication

def apply_jobs():
    criteria = "Software Engineer, Remote"
    resume = "data/resumes/my_resume.pdf"

    job_finder = JobFinder()
    matcher = ResumeMatcher()
    updater = ResumeUpdater()
    submitter = ApplicationSubmitter()
    logger = LoggingAgent()

    job_task = FindJobs(job_finder, criteria)
    jobs = job_task.run()

    match_task = MatchResume(matcher, jobs, resume)
    best_jobs = match_task.run()

    for job in best_jobs[:3]:
        update_task = UpdateResume(updater, resume, job)
        updated_resume = update_task.run()
        submit_task = SubmitApplication(submitter, job)
        status = submit_task.run()
        log_task = LogApplication(logger, job, status)
        log_task.run()
