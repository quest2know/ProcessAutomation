from datetime import datetime
from pathlib import Path
import schedule
import time
from utils.logger import setup_logger
from collector import main as collect_data, load_config   
from utils.cleaner import   delete_old_files, cleanup_log_file

config = load_config()
log = setup_logger(config['paths']['log_file']) # since we have one log filename we can use it directly in scheduler as well as collector instead of passing logger around.

def cleanup():
    # Clean up old report files and log files before starting the scheduler
    delete_old_files(Path(config['paths']['report_path']), config['cleanup']['report_days_to_keep'], log)
    cleanup_log_file(Path(config['paths']['log_file']), config['cleanup']['log_days_to_keep'], log)   
    delete_old_files(Path(config['paths']['db_path']), config['cleanup']['snapshot_days_to_keep'], log)
    
def scheduled_job():
    log.info(f"******Scheduled job started {datetime.now()} ********")
    cleanup()  
    collect_data()
    log.info("******Scheduled job finished*******")
    

def run_scheduler():
    # Run every hour
    schedule.every().minute.do(scheduled_job)   #for testing purpose changed to every minute, change to .hour for hourly run.   
    
    log.info("Scheduler started. Running every hour...")
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
       
    run_scheduler() 
