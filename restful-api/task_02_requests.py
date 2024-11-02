#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    print(f"Status Code: 200")

    if response.status_code == 200:
        response_json = response.json()

        for iterator_dict in response_json:
            print(iterator_dict["title"])


def fetch_and_save_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
        response_json = response.json()

        posts_data = []
        for iterator_post in response_json:
            new_dict = {
                    "id": iterator_post["id"],
                    "title": iterator_post["title"],
                    "body": iterator_post["body"]
            }
            posts_data.append(new_dict)

        with open("posts.csv", mode="w", newline="") as file_csv:
            writer = csv.DictWriter(
                    file_csv, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(posts_data)


if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
