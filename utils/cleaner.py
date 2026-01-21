from datetime import datetime,timedelta

def delete_old_files(report_dir, days_to_keep, logger):
    """Cleans up old files older than the specified number of days."""
    now = datetime.now()
    cutoff_date = now - timedelta(days=days_to_keep)
    logger.info(f"deleting files older than {cutoff_date.strftime('%Y-%m-%d %H:%M:%S')}")

    for rep_file in report_dir.glob("*.*"):    #
        file_modified_time = datetime.fromtimestamp(rep_file.stat().st_mtime) # get last modified time
        if file_modified_time < cutoff_date:
            try:
                rep_file.unlink()
                logger.info(f"Deleted old  files: {rep_file.name}")
            except Exception as e:
                logger.error(f"Error deleting file {rep_file.name}: {e}")
            
    logger.info(f"Old files cleanup completed. - {report_dir}")

def cleanup_log_file(log_file_path, days, logger):
        """Cleans up the log file to keep only the last 'days' days entries."""
        recent_lines = []
        try:
            with log_file_path.open('r', encoding='utf-8', errors = "ignore") as f:
               for line in f:
            
                    if line.startswith('['):  # Assuming log lines start with a timestamp
                            log_date_str = line.split(']')[0][1:]  # Extract date string
                            log_date = datetime.strptime(log_date_str, '%Y-%m-%d %H:%M:%S,%f')
                            if log_date >= datetime.now() - timedelta(days=days):
                                recent_lines.append(line)
                    
                    else:
                        try:
                            log_date_str = line[0:20]  # Extract date string
                            log_date = datetime.strptime(log_date_str, '%Y-%m-%d %H:%M:%S')
                            if log_date >= datetime.now() - timedelta(days=days):
                                    recent_lines.append(line)
                        except ValueError:
                            recent_lines.append(line)
                            print(f"Could not parse date from log line: {line.strip()}, date_str: {line[0:20]}, log_date: { datetime.strptime(log_date_str, '%Y-%m-%d %H:%M:%S,%f')} ")
            with log_file_path.open('w', encoding='utf-8', errors = "ignore") as f:
                f.writelines(recent_lines)  
                        
        except Exception as e:
            logger.error(f"Error cleaning up log file: {e}")