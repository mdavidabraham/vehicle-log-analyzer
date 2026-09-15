import argparse
import re


def analyze_log(filepath):
	counts = {"ERROR": 0, "WARNING": 0}

	try:
		with open(filepath, "r", encoding="utf-8", errors="replace") as log_file:
			for line_number, line in enumerate(log_file, start=1):
				match = re.search(r"\b(ERROR|WARNING)\b", line, re.IGNORECASE)
				if match:
					level = match.group(1).upper()
					counts[level] += 1
					print(f"{level} (line {line_number}): {line.rstrip()}")
	except FileNotFoundError:
		print(f"Log file not found: {filepath}")
		return

	print("\nSummary:")
	print(f"ERROR lines: {counts['ERROR']}")
	print(f"WARNING lines: {counts['WARNING']}")


if __name__ == "__main__":
	parser = argparse.ArgumentParser(
		description="Find and count ERROR and WARNING messages in a vehicle log file."
	)
	parser.add_argument(
		"log_file",
		nargs="?",
		default="vehicles.log",
		help="Path to the vehicle log file (default: vehicles.log)",
	)
	analyze_log(parser.parse_args().log_file)
