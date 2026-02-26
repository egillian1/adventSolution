import os

def count_safe_reports(path: str) -> int:
    try:
        safe_count = 0
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                report = [int(x) for x in line.split()]
                if check_report_is_safe(report):
                    safe_count += 1

        return safe_count
    except FileNotFoundError:
        print(f"File not found: {path}")
    except Exception as e:
        print(f"Error reading {path}: {e}")

def check_report_is_safe(report: list[int]) -> bool:
    # This case is not mentioned in the rules specifically, but since the constraint is that
    # the reactors can only handle gradual change, no change is probably bad.
    if len(report) <= 1:
        return False

    if len(report) == 2:
        difference = abs(report[0] - report[1])
        return difference < 1 or difference > 3
    
    levels_increased = False
    levels_decreased = False
    for i in range(len(report) - 1):
        difference = abs(report[i] - report[i + 1])
        if(difference < 1 or difference > 3):
            return False

        if report[i] < report[i + 1]:
            levels_increased = True
        elif report[i] > report[i + 1]:
            levels_decreased = True
        
        if levels_increased and levels_decreased:
            return False

    return True
        
input_path = input("Enter the name of the report file: ")
current_dir = os.path.dirname(__file__)
report_file_path = os.path.join(current_dir, 'report_files/' ,input_path)
safe_reports = count_safe_reports(report_file_path)
if safe_reports is not None:
    print("Number of safe reports in {}: {}".format(input_path, safe_reports))
else:
    print("Could not count safe reports due to an error. Please check the file path and try again.")
