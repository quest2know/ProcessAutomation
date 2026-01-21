from pathlib import Path
from datetime import datetime


def create_summary_report(normalized,summary_path,logger):
    """Creates a summary report from data fetched from three different APIs."""
    base = Path(summary_path)
    base.mkdir(exist_ok=True, parents=True)  # Create the directory if it doesn't exist
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    report_file = base / f'summary_report_{timestamp}.txt'
    logger.info(f"Creating summary report at: {report_file.resolve()}")
    with report_file.open('w',encoding='utf-8') as f:
        f.write(" Daily Data Summary Report\n")
        f.write("==========================\n\n")
        
        f.write("GitHub Stars: ")
        f.write(str(normalized["github_repo"]['stars'])  )
        f.write("\n\n")
        
        f.write("Bitcoin USD: ")
        f.write(str(normalized["bitcoin_price"]['usd']))
        f.write('          ')
        f.write("Ethereum USD: ")
        f.write(str(normalized["ethereum_price"]['usd']) )
        f.write("\n\n")
        
        f.write("Bitcoin EUR: ")
        f.write(str(normalized["bitcoin_price"]['eur'])       )  
        f.write('          ')
        f.write("Ethereum EUR: ")
        f.write(str(normalized["ethereum_price"]['eur']) )
        f.write("\n\n")


        f.write("Bitcoin GBP: ")
        f.write(str(normalized["bitcoin_price"]['gbp']))
        f.write('          ')
        f.write("Ethereum GBP: ")
        f.write(str(normalized["ethereum_price"]['gbp'])  )
        f.write("\n\n")

        
        f.write("User Name: ")
        f.write(str(normalized["user_info"]['name'] ))
        f.write("\n\n")

        f.write("User Email: ")
        f.write(normalized["user_info"]['email'])
        f.write("\n\n")
    print(f"Summary report created at {report_file.resolve()}")
    logger.info(f"Summary report created at: {report_file.resolve()}")
    f.close()
        
    return report_file