import csv
import argparse
from datetime import datetime
from collections import defaultdict


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_file", type=str, required=True, help="We need a set of data in a file.")
    parser.add_argument("-s", "--start_date", type=str,required=True, help="start date")
    parser.add_argument("-e","--end_date", type=str,required=True, help="end date")
    parser.add_argument("-o", "--output_file", type=str, help="specify a file where you want your results if no output file is specified otout will be printed to stout")

    args = parser.parse_args()

    
    s_date = datetime.strptime(args.start_date, "%Y-%m-%d")
    e_date = datetime.strptime(args.end_date, "%Y-%m-%d")

    counts = defaultdict(int)

    with open(args.input_file) as f: 
        reader = csv.DictReader(f)
        for row in reader: 
            c_date = datetime.strptime(row["Created Date"].split()[0], "%m/%d/%Y")
            if s_date <= c_date <= e_date:
                    key = (row["Complaint Type"], row["Borough"])
                    counts[key] += 1
    
    
    output_lines = ["complaint type,borough,count"]
    for (complaint, borough), count in sorted(counts.items()):
        output_lines.append(f"{complaint},{borough},{count}")

    if args.output_file:
        with open(args.output_file, "w") as f:
            f.write("\n".join(output_lines))
        print(f"Results saved to {args.output_file}")
    else:
        print("\n".join(output_lines))

    return




if __name__ == "__main__":
    main()
     