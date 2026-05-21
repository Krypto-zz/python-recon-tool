import json
from datetime import datetime

def report_export(report):
    now = datetime.now()
    now_str = now.strftime("%Y-%m-%d-%H-%S")
    rout_file = f"reports/scanning{now_str}.json"

    with open(rout_file, "w") as r:
        json.dump(report, r, indent=4)
    
    print(f"Guardado en reports. \nArchivo: {rout_file}")


