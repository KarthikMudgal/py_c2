active_client = 1
pwned_dict = {1: "larry@system@epoch_time",
              2: "curly@system2@epoch_time",
              3: "moe@system3@epoch_time"}

# Print pwned systems and active session information to our screen
print("Available pwned systems:")
print_last = None
for key, value in pwned_dict.items():
    if key == active_client:
        print_last = str(key) + " - " + value
    else:
        print(key, "-", value)

print("\nYour active session:", print_last, sep="\n")