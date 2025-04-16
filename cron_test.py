from datetime import datetime

with open("/tmp/cron_test_output.txt", "a") as f:
    f.write(f"CRON ran at {datetime.now()}\n")
