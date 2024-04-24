# Copyright (C) 2023 by Artem Khrapov (kabachuha)
# Read LICENSE for usage terms.

import launch

import os

req_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "requirements.txt")

with open(req_file) as file:

    for lib in file:

        lib = lib.strip()

        if not launch.is_installed(lib):
            launch.run_pip(f"install {lib}", f"clear object requirement: {lib}")

# Install neuralgym from Git with specific commit hash
#neuralgym_repo_url = "https://github.com/nirnayroy/neuralgym.git"
#launch.run_pip(f"install git+{neuralgym_repo_url}", "clear object requirement: neuralgym")

#neuralgym_repo_url = "https://github.com/bg1szd/neuralgym"
neuralgym_repo_url = "https://github.com/RGX650/neuralgym-SDNEXT"
launch.run_pip(f"install git+{neuralgym_repo_url}")
