from git import Repo
import pandas as pd

def show_changed_lines(repo_path, commit_sha,project,commit_link):
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
            changes.append({'file_name': file_name, 'line_before': line[1:].strip(), 'line_after': '', 'reference': commit_sha,"project":project,"commit_link":commit_link})
        elif line.startswith('+') and not line.startswith('+++'):
            if changes and changes[-1]['line_after'] == '':
                changes[-1]['line_after'] = line[1:].strip()
            else:
                changes.append({'file_name': file_name, 'line_before': '', 'line_after': line[1:].strip(), 'reference': commit_sha,"project":project,"commit_link":commit_link})

    # save csv file to pandas dataframe
    df = pd.DataFrame(changes)
    df.to_csv(f'data/{project}_code_changes.csv', index=False)

repo_path = 'repos/lodash'
project_name ="lodash"
commit_sha = 'd8e069cc3410082e44eb18fcf8e7f3d08ebe1d4a'
commit_link='https://github.com/lodash/lodash/commit/d8e069cc3410082e44eb18fcf8e7f3d08ebe1d4a'

# repo_path = 'repos/mixin-deep'
# project_name ="mixin-deep"
# commit_sha = '8f464c8ce9761a8c9c2b3457eaeee9d404fa7af9'
# commit_link='https://github.com/jonschlinkert/mixin-deep/commit/8f464c8ce9761a8c9c2b3457eaeee9d404fa7af9'


# repo_path = 'repos/PooledWebSocket'
# project_name ="PooledWebSocket"
# commit_sha = '7b3b4e5c6be6d8a964296fa3c50e38dc07e9701d'
# commit_link='https://github.com/Eeems/PooledWebSocket/commit/7b3b4e5c6be6d8a964296fa3c50e38dc07e9701d'



# repo_path = 'repos/windows-build-tools'
# project_name ="windows-build-tools"
# commit_sha = '9835d33e68f2cb5e4d148e954bb3ed0221d98e90'
# commit_link='https://github.com/felixrieseberg/windows-build-tools/commit/9835d33e68f2cb5e4d148e954bb3ed0221d98e90'

# repo_path = 'repos/ejs'
# project_name ="ejs"
# commit_sha = '49264e0037e313a0a3e033450b5c184112516d8f'
# commit_link='https://github.com/mde/ejs/commit/49264e0037e313a0a3e033450b5c184112516d8f'

# repo_path = 'repos/KubePi'
# project_name ="KubePi"
# commit_sha = '0faa8c2018a265eac9d1d8021afbeeba06d92024'
# commit_link='https://github.com/1Panel-dev/KubePi/commit/0faa8c2018a265eac9d1d8021afbeeba06d92024'

# repo_path = 'repos/moment'
# project_name ="moment"
# commit_sha = '663f33e333212b3800b63592cd8e237ac8fabdb9'
# commit_link='https://github.com/moment/moment/commit/663f33e333212b3800b63592cd8e237ac8fabdb9'


# repo_path = 'repos/hostr'
# project_name ="hostr"
# commit_sha = '789a00047459fd80b6f0a9701a1378a47fb73ba8'

show_changed_lines(repo_path, commit_sha,project_name,commit_link)