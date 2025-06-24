import subprocess
import sys
import shutil

def run_command(command, use_shell=True):
    print(f'Running: {command}')
    subprocess.run(command, shell=use_shell, check=True)

def install_with_uv_or_pip(package):
    if shutil.which("uv"):
        try:
            run_command(f'uv pip install --system {package}')
        except subprocess.CalledProcessError:
            print(f"❌ Failed to install {package} using uv. Trying pip...")
            run_command(f'{sys.executable} -m pip install {package}')
    else:
        print("⚠️  uv not found. Installing using pip instead.")
        run_command(f'{sys.executable} -m pip install {package}')

def check_python_version():
    if sys.version_info < (3, 11):
        print("❌ Python 3.11 or later is required.")
        sys.exit(1)
    else:
        print(f"✅ Python version is {sys.version_info.major}.{sys.version_info.minor} — OK")

def install_jupyterlab():
    install_with_uv_or_pip("jupyterlab>=4.2")

def install_streamlit():
    install_with_uv_or_pip("streamlit>=1.40")

def install_git():
    if not shutil.which("git"):
        run_command('winget install --id Git.Git -e --source winget')
    else:
        print("✅ Git already installed")

def install_vscode():
    if not shutil.which("code"):
        run_command('winget install --id Microsoft.VisualStudioCode -e --source winget')
    else:
        print("✅ VS Code already installed")

def main():
    check_python_version()
    run_command(f'"{sys.executable}" -m pip install --upgrade pip')
    run_command(f'"{sys.executable}" -m pip install uv')
    install_jupyterlab()
    install_streamlit()
    install_git()
    install_vscode()

if __name__ == "__main__":
    main()
