import subprocess
import os


def git_push(repo_path, commit_message, remote_name, branch_name):
    os.chdir(repo_path)

    # Add all files in the directory to staging
    subprocess.run(["git", "add", "."])
    print("Added files to git")

    # Check if there are changes to be committed
    status_result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)

    if status_result.stdout:
        try:
            # Commit the changes
            subprocess.check_call(["git", "commit", "-m", commit_message])
            print("Committed changes")

            # Push the changes
            subprocess.check_call(["git", "push", remote_name, branch_name])
            print("Pushed changes to GitHub")

        except subprocess.CalledProcessError as e:
            print(f"Failed to push changes: {e}")
    else:
        print("No changes to commit.")


if __name__ == "__main__":
    # Change these variables to match your setup
    repo_path = "C:/Users/toto/Documents/GitHub3/newsletter002/newsletter3"
    commit_message = "Automated commit message"
    remote_name = "newsletter3"  # Ensure this matches your remote repository name
    branch_name = "main"

    git_push(repo_path, commit_message, remote_name, branch_name)
