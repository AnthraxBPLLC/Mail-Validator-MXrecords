import dns.resolver
import threading
import sys
import time
import re
import tqdm

# Define a function to validate the email
def validate_email(email):
    try:
        # Get the MX record for the email domain
        domain = email.split('@')[1]
        records = dns.resolver(domain, 'MX')
        mx_record = str(records[0].exchange)
        # If the MX record is found, the email is valid
        return True
    except:
        # If the MX record is not found, the email is not valid
        return False

# Define a function to handle the multithreading
def handle_threads(email_list, num_threads):
    # Split the email list into chunks based on the number of threads
    chunk_size = len(email_list) // num_threads
    chunks = [email_list[i:i + chunk_size] for i in range(0, len(email_list), chunk_size)]
    threads = []
    # Start a new thread for each chunk
    for chunk in chunks:
        thread = threading.Thread(target=process_chunk, args=(chunk,))
        thread.start()
        threads.append(thread)
    # Wait for all threads to finish
    for thread in threads:
        thread.join()

# Define a function to process each chunk of emails
def process_chunk(chunk):
    valid_emails = []
    invalid_emails = []
    for email in chunk:
        result = validate_email(email)
        if result:
            valid_emails.append(email)
        else:
            invalid_emails.append(email)
    with open('valid.txt', 'a') as valid_file:
        for email in valid_emails:
            valid_file.write(email + '\n')
    with open('invalid.txt', 'a') as invalid_file:
        for email in invalid_emails:
            invalid_file.write(email + '\n')
            def display_banner():
    print('''

██████╗ ██████╗     ███╗   ███╗ █████╗ ██╗██╗         ██╗   ██╗ █████╗ ██╗     ██╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
██╔══██╗██╔══██╗    ████╗ ████║██╔══██╗██║██║         ██║   ██║██╔══██╗██║     ██║██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██████╔╝██████╔╝    ██╔████╔██║███████║██║██║         ██║   ██║███████║██║     ██║██║  ██║███████║   ██║   ██║   ██║██████╔╝
██╔══██╗██╔═══╝     ██║╚██╔╝██║██╔══██║██║██║         ╚██╗ ██╔╝██╔══██║██║     ██║██║  ██║██╔══██║   ██║   ██║   ██║██╔══██╗
██████╔╝██║         ██║ ╚═╝ ██║██║  ██║██║███████╗     ╚████╔╝ ██║  ██║███████╗██║██████╔╝██║  ██║   ██║   ╚██████╔╝██║  ██║
╚═════╝ ╚═╝         ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝      ╚═══╝  ╚═╝  ╚═╝╚══════╝╚═╝╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
     '''                                                                                                                       

def handle_threads(email_list, num_threads):
    # Split the email list into chunks based on the number of threads
    chunk_size = len(email_list) // num_threads
    chunks = [email_list[i:i + chunk_size] for i in range(0, len(email_list), chunk_size)]
    threads = []
    # Start a new thread for each chunk
    for chunk in chunks:
        thread = threading.Thread(target=process_chunk, args=(chunk,))
        thread.start()
        threads.append(thread)
    # Use tqdm to display a progress bar for each thread
    for thread in tqdm.tqdm(threads, desc='Threads', unit='thread'):
        thread.join()
# Main function
if __name__ == '__main__':
    display_banner()
    email_list = []
    file_name = input('Enter the name of the .txt file: ')
    # Read the email list from the .txt file
    with open(file_name, 'r') as email_file:
        for line in email_file:
            email_list.append(line.strip())
    # Ask the user for the number of threads to use
    num_threads = int(input('Enter the number of threads (0-100): '))
    # Start the email validation process
    start = time.time()
    results = handle_threads(email_list, num_threads)
    end = time.time()
    # Calculate the total number of valid and invalid emails
    valid_count = 0
    invalid_count = 0
    for result in results:
        valid_count += result[0]
        invalid_count += result[1]
    print('Validation completed in', end - start, 'seconds.')
    print('Valid emails:', valid_count)
    print('Invalid emails:', invalid_count)
def validate_email_syntax(email):
    # Regular expression pattern for a valid email address
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email)
def validate_email(email):
    if validate_email_syntax(email):
        try:
            # Get the MX record for the email domain
            domain = email.split('@')[1]
            records = dns.resolver.query(domain, 'MX')
            mx_record = str(records[0].exchange)
            # If the MX record is found, the email is valid
            return True
        except:
            # If the MX record is not found, the email is not valid
            return False
    else:
        # If the email syntax is invalid, return False
        return False
def validate_email_syntax(email):
    # Regular expression pattern for a valid email address
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email)
def validate_email(email):
    if validate_email_syntax(email):
        try:
            # Get the MX record for the email domain
            domain = email.split('@')[1]
            records = dns.resolver.query(domain, 'MX')
            mx_record = str(records[0].exchange)
            # If the MX record is found, the email is valid
            return True
        except:
            # If the MX record is not found, the email is not valid
            return False
    else:
        # If the email syntax is invalid, return False
        return False
def handle_threads(email_list, num_threads):
    # Split the email list into chunks based on the number of threads
    chunk_size = len(email_list) // num_threads
    chunks = [email_list[i:i + chunk_size] for i in range(0, len(email_list), chunk_size)]
    threads = []
    # Start a new thread for each chunk
    for chunk in chunks:
        thread = threading.Thread(target=process_chunk, args=(chunk,))
        thread.start()
        threads.append(thread)
    # Use tqdm to display a progress bar for each thread
    for thread in tqdm.tqdm(threads, desc='Threads', unit='thread'):
        thread.join()
def validate_email(email): 
    if validate_email_syntax(email):
        try:
            # Get the MX record for the email domain
            domain = email.split('@')[1]
            records = dns.resolver.query(domain, 'MX')
            mx_record = str(records[0].exchange)
            # If the MX record is found, the email is valid
            return True
        except:
            # If the MX record is not found, the email is not valid
            return False   
    else:
        # If the email syntax is invalid, return False
        return False
def process_chunk(chunk):
    valid_emails = []
    invalid_emails = []
    for email in chunk:
        result = validate_email(email)
        if result:
            valid_emails.append(email)
        else:
            invalid_emails.append(email)
    with open('valid.txt', 'a') as valid_file:
        for email in valid_emails:
            valid_file.write(email + '\n')
    with open('invalid.txt', 'a') as invalid_file:
        for email in invalid_emails:
            invalid_file.write(email + '\n')
    return (len(valid_emails), len(invalid_emails))    

if __name__ == '__main__':
    display_banner()
    email_list = []
    # Read the email list from the .txt file
    with open('email_list.txt', 'r') as email_file:
        for line in email_file:
            email_list.append(line.strip())
    # Ask the user for the number of threads to use
    num_threads = int(input('Enter the number of threads (0-100): '))
    # Start the email validation process
    start = time.time()
    results = handle_threads(email_list, num_threads)
    end = time.time()
    # Calculate the total number of valid and invalid emails
    valid_count = 0
    invalid_count = 0
    for result in results:
        valid_count += result[0]
        invalid_count += result[1]
    print('Validation completed in', end - start, 'seconds.')
    print('Valid emails:', valid_count)
    print('Invalid emails:', invalid_count) #check all codes if its correct
  
