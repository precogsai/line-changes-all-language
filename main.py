import csv
from git import Repo

def extract_changed_lines(repo_path, commit_hash):
    repo = Repo(repo_path)
    commit = repo.commit(commit_hash)
    data = []

    for file in commit.stats.files:
        file_path = file
        diff = commit.diff(commit.parents[0], paths=file_path)
        
        for hunk in diff.iter_change_type('M'):
            for line in hunk.diff.splitlines():
                if line.startswith('+') or line.startswith('-'):
                    data.append([file_path, line.strip()])

    return data

def save_to_csv(data, output_file):
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['File', 'Changed Line'])
        writer.writerows(data)

# Example usage:
# https://github.com/moment/moment/commit/663f33e333212b3800b63592cd8e237ac8fabdb9
repo_path = '/path/to/your/repo'
commit_hash = '5aea738463960d81821c11ae7ade1d627a46bf32'
output_file = 'output.csv'

data = extract_changed_lines(repo_path, commit_hash)
save_to_csv(data, output_file)
