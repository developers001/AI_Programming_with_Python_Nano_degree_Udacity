def func(value1, value2):
    isV1Str = isinstance(value1, str)
    isV2Str = isinstance(value2, str)
    print("********** BEGIN **********")
    if isV1Str == isV2Str:
        print("{} + {} = {}".format(value1, value2, value1 + value2))
        if not isV1Str:
            print("{} - {} = {}".format(value1, value2, value1 - value2))
            print("{} * {} = {}".format(value1, value2, value1 * value2))
            if (value2 != 0) :
                print("{} / {} = {}".format(value1, value2, value1 / value2))
            else:
                print("{} is not dividable by {}".format(value1, value2))
    else:
        aString = value1 if isV1Str else value2
        aNum = int(value2 if isV1Str else value1)
        print("{} * {} = {}".format(value1, value2, aString * aNum))
    print("********** END **********")

def main():
    func(3, 2)
    func(3, 0)
    func(3, 4.0)
    func("hello", "world")
    func(2, "hello")
    func("hello",2)
    func(3.0, "world")

if __name__ == "__main__":
    main()
