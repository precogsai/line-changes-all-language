from git import Repo
import pandas as pd

def show_changed_lines(repo_path, commit_sha,project):
    repo = Repo(repo_path)
    commit = repo.commit(commit_sha)

    print(f"Showing changed lines for commit {commit_sha} in repository {repo_path}\n")

    changes = []

    diffs = repo.git.diff(commit.parents[0].hexsha, commit.hexsha, unified=0).splitlines()
    file_name = ''
    for line in diffs:
        if line.startswith('---') or line.startswith('+++'):
            file_name = line[6:]
        elif line.startswith('-') and not line.startswith('---'):
            changes.append({'file_name': file_name, 'line_before': line[1:].strip(), 'line_after': '', 'reference': commit_sha,"project":project})
        elif line.startswith('+') and not line.startswith('+++'):
            if changes and changes[-1]['line_after'] == '':
                changes[-1]['line_after'] = line[1:].strip()
            else:
                changes.append({'file_name': file_name, 'line_before': '', 'line_after': line[1:].strip(), 'reference': commit_sha,"project":project})

    # save csv file to pandas dataframe
    df = pd.DataFrame(changes)
    df.to_csv(f'data/{project}_code_changes.csv', index=False)



# repo_path = 'repos/moment'
# project_name ="moment"
# commit_sha = '663f33e333212b3800b63592cd8e237ac8fabdb9'
repo_path = 'repos/hostr'
project_name ="hostr"
commit_sha = '789a00047459fd80b6f0a9701a1378a47fb73ba8'

show_changed_lines(repo_path, commit_sha,project_name)