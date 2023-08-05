from apscheduler.schedulers.blocking import BlockingScheduler
from selenium import webdriver
from selenium.webdriver.common.by import By
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
from datetime import datetime, timedelta

root = tk.Tk()
root.withdraw()
messagebox.showinfo("Title", "Hello World")

def get_user_info():
    # Create a new tkinter window
    root = tk.Tk()
    # Hide the main window
    root.withdraw()
    
    first_name = simpledialog.askstring("Input", "Enter your first name",
                                        parent=root)
    last_name = simpledialog.askstring("Input", "Enter your last name",
                                       parent=root)
    confirmation_number = simpledialog.askstring("Input", "Enter your confirmation number",
                                                 parent=root)
    # Get check-in date and time
    check_in_datetime = simpledialog.askstring("Input", "Enter the date and time for check-in (format: 'YYYY-MM-DD HH:MM')",
                                               parent=root)

    # Convert check-in date and time to datetime object
    check_in_datetime = datetime.strptime(check_in_datetime, '%Y-%m-%d %H:%M')

    # Add 5 seconds to the check-in time
    check_in_datetime = check_in_datetime + timedelta(seconds=5)

    return first_name, last_name, confirmation_number, check_in_datetime

def check_in():
    first_name, last_name, confirmation_number, check_in_datetime = get_user_info()
    driver = webdriver.Chrome()
    driver.get("https://www.southwest.com/air/check-in/index.html")

    # Login to site using credentials
    confirmation_input = driver.find_element(By.ID, "confirmationNumber")
    first_name_input = driver.find_element(By.ID, "passengerFirstName")
    last_name_input = driver.find_element(By.ID, "passengerLastName")
    check_in_button = driver.find_element(By.ID, "form-mixin--submit-button")

    confirmation_input.send_keys(confirmation_number)
    first_name_input.send_keys(first_name)
    last_name_input.send_keys(last_name)

    check_in_button.click()

    # Handle MFA
    # Handling MFA would depend on the specific implementation.

scheduler = BlockingScheduler()
# Get user info and check-in date and time
first_name, last_name, confirmation_number, check_in_datetime = get_user_info()
# Schedule the check-in job
scheduler.add_job(check_in, 'date', run_date=check_in_datetime) 
scheduler.start()