from ros2cli.command import CommandExtension
from ros2pkg.api import package_name_completer
from ros2pkg.api import PackageNotFound
from ros2install.api import get_repo, build_pkg, ROSPATH

class InstallCommand(CommandExtension):
    def add_arguments(self, parser, cli_name):
        #self._subparser = parser
        #verb_extensions = get_verb_extensions('ros2install.verb')
        #add_subparsers(parser, cli_name, '_verb', verb_extensions, required=False)
        try:
            from argcomplete.completers import SuppressCompleter
        except ImportError:
            pass
        else:
            arg.completer = SuppressCompleter()
        arg = parser.add_argument(
            'package_name',
            help='Name of the remote ROS package(example: github.com/myorg/rospkg_name)')
        arg.completer = package_name_completer

        arg = parser.add_argument(
            'branch',
            help='Branch of the remote ROS package(example: master, dashing, eloquent...)')
        arg.completer = package_name_completer


    def main(self, *, parser, args):
        if not ROSPATH:
            raise RuntimeError(f"ROSPATH env var is not set!")
        
        git_url = 'https://' + args.package_name
        try:
            repo = get_repo(git_url, args.branch)
            build_pkg(ROSPATH, repo.repo)
        except Exception as e:
            #raise RuntimeError(f"Failed to clone repo '{args.package_name}': {e}")
            print(e)
