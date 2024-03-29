from common.util import build_path
from data.numpy_manager import NumpyManger


def test_data():
    npm = NumpyManger()

    data = npm.load_file(build_path('assets/sample1.csv'))
    rows, cols = data.shape

    print(cols)


def main():
    test_data()


if __name__ == '__main__':
    main()
