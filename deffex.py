#!/usr/bin/env python3
import os
from github import Github
from dotenv import load_dotenv

class Deffex:
    def __init__(self):
        load_dotenv()
        self.github = None
        self.user_info = {
           "name": os.getenv("YOUR_NAME", "DEFFEX"),  # Default if not in .env
            "email": os.getenv("YOUR_EMAIL", "deffex_adnan@vk.com")
        }

    def show_banner(self):
        print(f"""
        ██████╗ ███████╗███████╗███████╗██╗  ██╗
        ██╔══██╗██╔════╝██╔════╝██╔════╝╚██╗██╔╝
        ██║  ██║█████╗  █████╗  █████╗   ╚███╔╝ 
        ██║  ██║██╔══╝  ██╔══╝  ██╔══╝   ██╔██╗ 
        ██████╔╝███████╗██║     ███████╗██╔╝ ██╗
        ╚═════╝ ╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝
        DEFFEX - GitHub Terminal Tool
        Created by: {self.user_info['name']}
        Contact: {self.user_info['email']}
        """)

    def login(self):
        token = os.getenv("GITHUB_TOKEN")
        if not token:
            from getpass import getpass
            token = getpass("Enter GitHub Token: ")

        try:
            self.github = Github(token)
            user = self.github.get_user()
            print(f"✅ Logged in as: {user.login}")
            return True
        except Exception as e:
            print(f"❌ Error: {e}")
            return False

    def show_repos(self):
        if not self.github:
            print("⚠️ Please login first (option 1)")
            return

        print("\n📂 Your GitHub Repositories:")
        for repo in self.github.get_user().get_repos():
            print(f"- {repo.name} ({'🔒 Private' if repo.private else '🌍 Public'})")

def main():
    tool = Deffex()
    tool.show_banner()

    while True:
        print("\n🔹 Menu:")
        print("1. Login to GitHub")
        print("2. List My Repositories")
        print("3. Exit")

        choice = input("Choose (1-3): ").strip()

        if choice == "1":
            tool.login()
        elif choice == "2":
            tool.show_repos()
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()
