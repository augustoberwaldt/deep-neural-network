import sys
import argparse
from src.app import Application


def main():

    ar = argparse.ArgumentParser()    
     
    ar.add_argument("-d", "--dataset", required=True,
	help="path to input dataset of images") 

    args = vars(ar.parse_args())

    app = Application(args)
    app.run()


if __name__ == '__main__':
    main()
