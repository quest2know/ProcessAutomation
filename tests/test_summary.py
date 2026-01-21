"""  testing if summary prints when names have different language accents... This was a bug earlier converted to a test. Code AI generated-microsoft copilot assisted   
"""

import pytest
from utils import summary
import json
from pathlib import Path
from unittest.mock import Mock


# Fixture with mock input

@pytest.fixture
def normalized_data():
    # Build the path relative to the test file
    file_path = Path(__file__).parent / "mock_data" / "testinputnormalized.json"
    with open(file_path, "r") as f:
        data = json.load(f)
    return data



def test_create_summary_report(tmp_path,normalized_data):
#arrange
    # Create a mock logger
    mock_logger = Mock()

    # Define the output file path
    output_path = tmp_path 
#act
    # Call the function with mock data
    report_file = summary.create_summary_report(normalized_data, output_path, mock_logger)

#assert - file was created
    assert report_file.exists()
    print(report_file/"summary_report.txt")
    assert report_file.name == "summary_report.txt"

#a
    
    report_content = Path(report_file).read_text(encoding="utf-8")
        # report_content = f.read()

    # Check if specific names with accents are in the report
    assert "Barış" in report_content
    assert " Düşenkalkar" in report_content        

# # Suppose create_summary_report returns just the directory path
# output_dir = create_summary_report(normalized_data, summary_path, logger)

# # Find all files in that directory
# files = list(Path(output_dir).glob("*.txt"))
# assert len(files) == 1   # or whatever number you expect

# report_file = files[0]
# content = report_file.read_text(encoding="utf-8")
# assert "Daily Data Summary Report" in content
