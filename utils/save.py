from pathlib import Path
import json
from  datetime import datetime

def save_snapshot(data, db_path, logger):
    """Saves the given data snapshot to a timestamped JSON file in the specified directory."""
    base = Path(db_path)
    base.mkdir(exist_ok=True, parents=True)  # Create the directory if it doesn't exist
    logger.info(f"Saving snapshot to directory: {base.resolve()}")
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    file_name = base / f'snapshot_{timestamp}.json'
    logger.info(f"Snapshot file will be: {file_name.resolve()}")    
    #  we can also use file_name.write_text(json.dumps(data, indent=4))
    with file_name.open('w') as f:
        json.dump(data, f, indent=4)  # Write data as formatted JSON
    
    print(f"Snapshot saved to {file_name.resolve()}")

    return file_name

def write_to_master(data,master_file, logger):
    """Appends the given data to a master JSON file."""
    Path(master_file).parent.mkdir(exist_ok=True, parents=True)  # Ensure the directory exists
    logger
    with open(master_file,'a') as f:
        f.write(json.dumps(data)+'\n')  # Write json data as unformatted line
    logger.info(f"Appended data to master file: {master_file}")
    print(f"Data appended to master file at {master_file}")
    return master_file