from config.dask_config import start_dask
from ingestion.loader import load_logs
from ingestion.parser import parse_log_line
import time

def main():
    client = start_dask()
    print(client)
    print(f"Dask dashboard available at: {client.dashboard_link}")
    print("\n" + "="*50)

    bag = load_logs('data/sample_log.log')
    parsed = bag.map(parse_log_line).filter(lambda x: x is not None)

    result = parsed.compute()
    print("\nParsed Log Entries:")
    for log in result:
        print(log)
    print("\n" + "="*50)
    print("Dashboard running at : http://127.0.0.1:8790/status")
    print("Press Ctrl+C to stop the script and shut down the Dask cluster.")
    
    # Keep the script running to allow dashboard access
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down Dask Cluster...")
        client.close()

if __name__ == "__main__":
    main()