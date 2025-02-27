import crewai
from workflows.apply_pipeline import apply_jobs

def main():
    print("Starting Automatic Job Application Agent...")
    apply_jobs()
    print("Job application process completed.")

if __name__ == "__main__":
    main()