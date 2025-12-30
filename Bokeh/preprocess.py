import csv
from datetime import datetime

CREATED_COL = "Created Date"
CLOSED_COL  = "Closed Date"
ZIP_COL     = "Incident Zip"

def parse_dt(s):
    if not s:
        return None
    for fmt in ("%m/%d/%Y %I:%M:%S %p", "%m/%d/%Y %H:%M", "%Y-%m-%d %H:%M:%S", "%Y-%m-%d"):
        try:
            return datetime.strptime(s, fmt)
        except ValueError:
            pass
    return None

def month_key(dt):
    return f"{dt.year:04d}-{dt.month:02d}"

def main():
    in_path = "../data/311_Service.csv"  
    out_zip = "monthly_zip_averages.csv"
    out_all = "monthly_all_averages.csv"

    by_zip = {}
    by_all = {}

    with open(in_path, "r", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            z = (row.get(ZIP_COL) or "").strip()
            if not z:
                continue

            cr = parse_dt(row.get(CREATED_COL))
            cl = parse_dt(row.get(CLOSED_COL))
            if not cr or not cl:
                continue

            # --- filter only 2024 ---
            if cl.year != 2024:
                continue

            hrs = (cl - cr).total_seconds() / 3600.0
            if hrs < 0:
                continue

            m = month_key(cl)
            by_zip.setdefault((m, z), [0.0, 0])
            by_zip[(m, z)][0] += hrs
            by_zip[(m, z)][1] += 1

            by_all.setdefault(m, [0.0, 0])
            by_all[m][0] += hrs
            by_all[m][1] += 1

    # Write per-zip CSV
    with open(out_zip, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["month", "zipcode", "avg_hours"])
        for (m, z), (s, n) in sorted(by_zip.items()):
            w.writerow([m, z, round(s / n, 2)])

    # Write overall CSV
    with open(out_all, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["month", "avg_hours"])
        for m, (s, n) in sorted(by_all.items()):
            w.writerow([m, round(s / n, 2)])

if __name__ == "__main__":
    main()
