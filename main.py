import sys

from src.app import Application
from pyspark.ml.classification import LogisticRegression

from pyspark import SparkConf, SparkContext
from pyspark.ml.regression import LinearRegression


def main():
    r = Application()
    r.run()


if __name__ == '__main__':
    main()
