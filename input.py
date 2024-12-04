"""
Defines a function to get puzzle input and save it as a text file.
"""

import os

import requests
from dotenv import load_dotenv

load_dotenv()


def save_input(year: int, day: int) -> None:
    url = "https://adventofcode.com/" + str(year) + "/day/" + str(day) + "/input"
    cookies = {"session": os.getenv("session")}
    result = requests.get(url, cookies=cookies)
    with open("input.txt", "w") as file:
        file.write(result.text)
