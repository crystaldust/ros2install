import git
import os
import subprocess
import giturlparse

ROSPATH = '/tmp'
if 'ROSPATH' in os.environ:
    ROSPATH = os.environ['ROSPATH']

def build_pkg(cwd, pkg_name=""):
    print(cwd)
    build_cmd = ["colcon", "build"]

    if pkg_name:
        build_cmd += ["--packages-select ", pkg_name]

    print(build_cmd)
    build_process = subprocess.run(build_cmd, cwd=cwd)
    return build_process

# from url to:
# protocol
# source_platform
# organization
# repo_name
# branch or commit or tag
def parse_git_url(url):
    pass

# https://github.com/ros-perception/laser_geometry/
# https://github.com/ros-perception/vision_opencv
def get_repo(repo_url):
    repo = giturlparse.parse(repo_url)
    repo_url = 'https://github.com/ros-perception/laser_geometry'
    repo_source_platform = 'github.com'
    repo_org = 'ros-perception'
    repo_name = 'laser_geometry'
    repo_branch = 'eloquent'

    repo_path = '{}/src/{}'.format(ROSPATH, repo_name)
    print(repo_path)
    #exit(0)

    try:
        repo = git.Repo.clone_from(repo_url, repo_path, branch=repo_branch)
    except Exception as e:
        print(e)
        print(type(e))
        print(e.command)
        print(e.status)
        print(e.stderr)
        if e.status == 128:
            print('TODO: Look into the path and see if it\'s the same remote repo')


if __name__ == '__main__':
    ROSPATH_SRC = os.environ['ROSPATH'] + '/src'
    get_repo('hhhhhhtptpgit')
    #  build_pkg(ROSPATH_SRC, 'vision_opencv')
    build_pkg(ROSPATH_SRC)
