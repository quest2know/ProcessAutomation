""" program will call utils and collect data from APIs and create a summary report while logging the activities. and creating files with timestamped snapshots and a master file appending all data"""


from utils.api import fetch_data_from_api
from utils.save import save_snapshot, write_to_master   
from utils.summary import create_summary_report
from utils.logger import setup_logger

import os
import yaml

def load_config():
    """Load configuration from a YAML file."""
    print(f"current working directory: {os.getcwd()}")
    with open('config.yaml', 'r') as f:
        config = yaml.safe_load(f)
    
    return config

def normalized_data(all_data):
    """Normalize and combine data from different APIs."""
    normalized = {}
    # Example normalization logic (to be customized based on actual data structure)
    if 'github' in all_data:
        github_data = all_data['github']
        normalized['github_repo'] = {
            'name': github_data.get('name'),
            'stars': github_data.get('stargazers_count'),
            'forks': github_data.get('forks_count')
        }
    if 'crypto_usd' or 'crypto_eur' or 'crypto_gbp' in all_data:
        print("found crypto data:")
        crypto_data ={}
        crypto_data['crypto_usd'] = all_data['crypto_usd']
        crypto_data['crypto_eur'] = all_data.get('crypto_eur',{})
        crypto_data['crypto_gbp'] =  all_data.get('crypto_gbp', {})

        print(f" Bitcoin data : {crypto_data}")
        normalized['bitcoin_price'] = {
            'usd': crypto_data.get('crypto_usd',{}).get('bitcoin', {}).get('usd', {}),
            'eur': crypto_data.get('crypto_eur',{}).get('bitcoin', {}).get('eur', {}),
            'gbp': crypto_data.get('crypto_gbp',{}).get('bitcoin', {}).get('gbp', {})
        }
        normalized['ethereum_price'] = {
            'usd': crypto_data.get('crypto_usd',{}).get('ethereum', {}).get('usd', {}),
            'eur': crypto_data.get('crypto_eur',{}).get('ethereum', {}).get('eur', {}),
            'gbp': crypto_data.get('crypto_gbp',{}).get('ethereum', {}).get('gbp', {})
            
        }
    if 'user' in all_data:
        user_data = all_data['user']
        normalized['user_info'] = {
            'name': user_data.get('results', [{}])[0].get('name', {}).get('first', '') + ' ' + user_data.get('results', [{}])[0].get('name', {}).get('last', ''),
            'email': user_data.get('results', [{}])[0].get('email', '')
        }
    return normalized

def main():
    config = load_config()
    logger = setup_logger(config['paths']['log_file']) 
    logger.info("Starting data collection process.")

    all_data = {

         'github': fetch_data_from_api(config['apis']['github'], logger),  
         'crypto_usd': fetch_data_from_api(config['apis']['crypto_usd'], logger),  
         'crypto_eur': fetch_data_from_api(config['apis']['crypto_eur'], logger),
         'crypto_gbp': fetch_data_from_api(config['apis']['crypto_gbp'], logger),
         'user': fetch_data_from_api(config['apis']['user'], logger)     
    }
    # 
    logger.info(f"Data fetched from all APIs...{all_data}")
    normalized = normalized_data(all_data)
    snapshot_path = save_snapshot(normalized, config['paths']['db_path'], logger)
    master_file = write_to_master(normalized, config['paths']['master_file'], logger)
    report_path = create_summary_report(normalized, config['paths']['report_file'], logger)
    logger.info("Data collection process completed.")
    print(f"Snapshot saved at: {snapshot_path}")    
    print(f"Master file updated at: {master_file}")
    print(f"Summary report created at: {report_path}")



if __name__ == "__main__":
    main()
""" program will call utils and collect data from APIs and create a summary report while logging the activities. and creating files with timestamped snapshots and a master file appending all data"""