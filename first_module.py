print("First module: this will always be run, directly or imported")
print("First module's name: {}".format(__name__))

def main():
# this will be run only if called from the second module as first_module.main()

    print("First module: main function")


if __name__ == '__main__':
    main()
