import time
from datetime import datetime as dt

hosts_path = 'C:\\Windows\\System32\\drivers\\etc\\hosts'
redirect_ip = '127.0.0.1'
website_list = ['www.facebook.com', 'facebook.com', 'www.twitter.com', 'twitter.com']

def block_websites(start_hour, end_hour):
    while True:
        # Get the current time
        now = dt.now()

        # Check if the current time is within the specified block hours
        if dt(now.year, now.month, now.day, start_hour) < now < dt(now.year, now.month, now.day, end_hour):
            print("Working hours. Websites blocked.")

            # Open the hosts file and add redirections for the specified websites
            with open(hosts_path, 'r+') as file:
                content = file.read()
                for website in website_list:
                    if website in content:
                        pass  # Website already blocked
                    else:
                        file.write(redirect_ip + ' ' + website + '\n')

        else:
            print("Fun hours. Websites unblocked.")

            # Open the hosts file and remove redirections for the specified websites
            with open(hosts_path, 'r+') as file:
                content = file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in website_list):
                        file.write(line)
                file.truncate()

        time.sleep(5)  # Check every 5 seconds (adjust as needed)

if __name__ == "__main__":
    # Set your working hours (24-hour format)
    start_hour = 9
    end_hour = 17

    block_websites(start_hour, end_hour)
