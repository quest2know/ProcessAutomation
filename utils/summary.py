from pathlib import Path



def create_summary_report(normalized,summary_path,logger):
    """Creates a summary report from data fetched from three different APIs."""
    base = Path(summary_path)
    base.mkdir(exist_ok=True, parents=True)  # Create the directory if it doesn't exist
    report_file = base / 'summary_report.txt'
    logger.info(f"Creating summary report at: {report_file.resolve()}")
    with report_file.open('w') as f:
        f.write(" Daily Data Summary Report\n")
        f.write("==========================\n\n")
        
        f.write("GitHub Stars: ")
        f.write(str(normalized["github_repo"]['stars']) + "\n\n")
        
        f.write("Bitcoin USD: ")
        f.write(str(normalized["bitcoin_price"]['usd']))
        f.write('          ')
        f.write("Ethereum USD: ")
        f.write(str(normalized["ethereum_price"]['usd']))  
        f.write("\n\n")
        
        f.write("Bitcoin EUR: ")
        f.write(str(normalized["bitcoin_price"]['eur']) )         
        f.write('          ')
        f.write("Ethereum EUR: ")
        f.write(str(normalized["ethereum_price"]['eur']))  
        f.write("\n\n")


        f.write("Bitcoin GBP: ")
        f.write(str(normalized["bitcoin_price"]['gbp']))
        f.write('          ')
        f.write("Ethereum GBP: ")
        f.write(str(normalized["ethereum_price"]['gbp'])  )
        f.write("\n\n")

        
        f.write("User Name: ")
        f.write(str(normalized["user_info"]['name']) + "\n\n")

        f.write("User Email: ")
        f.write(str(normalized["user_info"]['email']) + "\n\n")
  
    print(f"Summary report created at {report_file.resolve()}")
    logger.info(f"Summary report created at: {report_file.resolve()}")
        
    return report_file