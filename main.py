import sys
from pathlib import Path

ROOT = sys.path.append(str(Path(__file__).parent))
sys.path.append(str(ROOT))

from scheduler.scheduler import run_scheduler
from utils.logger    import setup_logger
from collector import load_config




config = load_config()

log = setup_logger(config['paths']['log_file']) # since we have one log filename we can use it directly in scheduler as well as collector instead of passing logger around.

def main():
    log.info("Application started")
    try:
        run_scheduler()
    except Exception as e:
        log.error(f"An error occurred: {e}")    
    except KeyboardInterrupt:
        log.info("Application interrupted by user")
        
    log.info("Application finished")


if __name__ == "__main__":
    main()
