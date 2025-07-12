import subprocess

def INSTALLER():
    def install_package(package_name):
        # Execute the pip install command
        result = subprocess.run(['pip', 'install', package_name], capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"Package '{package_name}' installed successfully.")
        else:
            print(f"Package installation failed. Error message: {result.stderr}")

    # Package name to install
    package_name = str(input("Package Name : "))

    # Install the package
    install_package(package_name)


while True:
    try:
        INSTALLER()
        print()
    except:
        print("Failed!! ... Try Again ...")