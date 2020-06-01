import git
import os
import subprocess
import giturlparse

ROSPATH = '/tmp'
if 'ROSPATH' in os.environ:
    ROSPATH = os.environ['ROSPATH']

def build_pkg(cwd, pkg_name=""):
    build_cmd = ["colcon", "build"]

    if pkg_name:
        build_cmd += ["--packages-select", pkg_name]

    print(build_cmd)
    build_process = subprocess.run(build_cmd, cwd=cwd)
    return build_process.returncode

# https://github.com/ros-perception/laser_geometry/
# https://github.com/ros-perception/vision_opencv
def get_repo(repo_url, branch='master'):
    repo = giturlparse.parse(repo_url)
    repo_path = '{}/src/{}'.format(ROSPATH, repo.repo)
    r = git.Repo.clone_from(repo_url, repo_path, branch=branch)
    # TODO some thing to return with r?
    return repo


