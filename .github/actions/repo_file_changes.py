""" Python script to get the list of added, modified, and deleted files in 
the current branch compared to the main branch. """

import subprocess
import json
import os


def get_git_diff():
    """
    Get the list of added, modified, and deleted files in the current
    branch compared to the main branch.
    """
    try:
        # Fetch the latest changes from the remote
        subprocess.run(["git", "fetch", "origin"], check=True)

        # Get the current branch name
        current_branch = (
            subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"])
            .strip()
            .decode("utf-8")
        )
        print(f"🔄 Current branch: {current_branch}")

        # Get the list of changed files
        result = subprocess.run(
            ["git", "diff", "--name-status", "origin/main...HEAD"],
            capture_output=True,
            text=True,
            check=True,
        )

        added_files = []
        modified_files = []
        deleted_files = []

        # Parse the output of `git diff --name-status`
        for line in result.stdout.splitlines():
            status, file_path = line.split("\t", 1)
            if status == "A":
                added_files.append(file_path)
            elif status == "M":
                modified_files.append(file_path)
            elif status == "D":
                deleted_files.append(file_path)

        return added_files, modified_files, deleted_files

    except subprocess.CalledProcessError as e:
        print(f"❌ Error running git command: {e}")
        return [], [], []


def main():
    """
    Main function to display the file changes.
    """
    github_repo = os.environ.get("INPUT_GITHUB-REPO")
    print(
        f"🚀 Checking file changes in the current branch of the repository {github_repo}...\n"
    )
    print("--------------------------------------------------------------------------")

    added, modified, deleted = get_git_diff()

    print("\n📄 **Added Files:**")
    print("\n".join(added) if added else "No files added.")

    print("\n📝 **Modified Files:**")
    print("\n".join(modified) if modified else "No files modified.")

    print("\n🗑️ **Deleted Files:**")
    print("\n".join(deleted) if deleted else "No files deleted.")

    # Optional: Export to JSON
    changes = {"added": added, "modified": modified, "deleted": deleted}

    with open("file_changes.json", "w", encoding="utf-8") as json_file:
        json.dump(changes, json_file, indent=4)

    print("\n✅ File change details saved to `file_changes.json`.")

    with open(os.getenv("GITHUB_OUTPUT", "/dev/null"), "a", encoding="utf-8") as file:
        file.write("aws-cloudformation=True\n")
        file.write("aws-lambda=True\n")
        file.write("aws-glue=True\n")
        file.write("aws-stepfunctions=False\n")
        file.write("aws-ecs=False\n")


if __name__ == "__main__":
    main()
