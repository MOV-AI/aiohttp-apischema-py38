import pathlib
import subprocess
from setuptools import setup
from setuptools.command.build_py import build_py as _build_py



class CustomBuild(_build_py):
    def run(self):
        destination_path = pathlib.Path(__file__).parent.resolve()

        # download swagger-ui
        swagger = f"{destination_path}/aiohttp_apischema/swagger-ui"
        download_cmd = f"curl -L $(curl -L 'https://api.github.com/repos/swagger-api/swagger-ui/releases?per_page=1' | jq -r .[0].tarball_url) | tar --wildcards --no-wildcards-match-slash -C {swagger} -xz 'swagger-api-swagger-ui-*/dist/' --strip-components=2"
        subprocess.run(f"mkdir -p {swagger}", shell=True, check=True)
        subprocess.run(download_cmd, shell=True, check=True)

        # patch according to original workflow
        patch_cmd = f"""sed -i -e 's/url:.*/url: document.getElementById("swagger-ui").dataset.url,/g' {swagger}/swagger-initializer.js"""
        subprocess.run(patch_cmd, shell=True, check=True)

        # Run the standard build process
        super().run()


setup(
    cmdclass={"build_py": CustomBuild},
)
