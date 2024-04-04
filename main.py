import subprocess
import os


def git_pull(repo_path, remote_name, branch_name):
    os.chdir(repo_path)
    try:
        # Pull changes from the remote repository, allowing unrelated histories
        subprocess.check_call(["git", "pull", "--allow-unrelated-histories", remote_name, branch_name])
        print("Pulled changes from GitHub")
    except subprocess.CalledProcessError as e:
        print(f"Failed to pull changes: {e}")


def git_push(repo_path, commit_message, remote_name, branch_name):
    os.chdir(repo_path)

    # Pull changes from the remote repository
    subprocess.run(["git", "pull", "--allow-unrelated-histories", remote_name, branch_name])
    print("Pulled changes from GitHub")

    # Add all files in the directory to staging
    subprocess.run(["git", "add", "."])
    print("Added files to git")

    # Check if there are changes to be committed
    status_result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
    if status_result.stdout.strip():  # Using strip() to remove any leading/trailing whitespace
        # Commit the changes if there are any
        subprocess.run(["git", "commit", "-m", commit_message])
        print("Committed changes")

        # Push the changes
        subprocess.run(["git", "push", remote_name, branch_name])
        print("Pushed changes to GitHub")
    else:
        print("No changes to commit.")


if __name__ == "__main__":
    # Change these variables to match your setup
    repo_path = "C:/Users/toto/Documents/GitHub3/newsletter002"
    commit_message = "Automated commit message"
    remote_name = "newsletter3"  # This should match your remote repository name
    branch_name = "main"

    # First try to pull changes from the remote repository
    git_pull(repo_path, remote_name, branch_name)

    # Then proceed with adding, committing, and pushing changes
    git_push(repo_path, commit_message, remote_name, branch_name)
