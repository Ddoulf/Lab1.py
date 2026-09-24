KB = 1024
MB = 1048576
GB = 1073741824

num_entries = input("Please enter the number of entries per second:" )
entry_size = input("Please enter the average number of bytes per entry: ")

bytes_per_minute= (int(num_entries) * int(entry_size)) / 60
bytes_per_hour = (int(num_entries) * int(entry_size)) / 3600
bytes_per_day = (int(num_entries) * int(entry_size)) / 86400

kb_size = bytes_per_minute / KB
mb_size = bytes_per_hour / MB
gb_size = bytes_per_day / GB

print("Storage Estimates")
print(f"Per minute: {kb_size}KB")
print(f"Per hour: {mb_size}MB")
print(f"Per day: {gb_size}GB")

#a) The storage required for 1 minutes worth of log entries, in KB
#b) The storage required for 1 hours worth of log entries, in MB
#c) The storage required for 1 days worth of log entries, in GB