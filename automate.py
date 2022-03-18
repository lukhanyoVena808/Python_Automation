import subprocess

"""Running C files with python Script"""


def main():

    # Running files using a make file
    # subprocess.call('make clean', shell=True)  # clean bin directory
    # subprocess.call('make', shell=True)   # make
    # subprocess.call('make run', shell=True)  # run files

    # Running a single C file
    file_name = ""
    # subprocess.call(f'gcc -g -Wall {fname}.c -o {fname}', shell=True)
    subprocess.call(f'{file_name}', shell=True)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
    except Exception as e:
        print("Error: {}".format(e))
