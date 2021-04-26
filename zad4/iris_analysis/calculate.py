from iris_analysis.io2.load import parseFileIntoColumns

def calculateFeature(path, feature_fun):
    columns = parseFileIntoColumns(path)
    return [ feature_fun(col) for col in columns ]

def getMean(col):
    return sum(col) / len(col)

def getMedian(col):
    sorted_vals = sorted(col)
    length = len(col)
    if length % 2 == 1:
        return sorted_vals[int(length / 2)]
    else:
        idx = int(length / 2)
        return 0.5 * (sorted_vals[idx - 1] + sorted_vals[idx])

def getStd(col):
    mean = getMean(col)
    squares = [ (v - mean) ** 2 for v in col ]
    sum_squares = sum(squares)
    return (sum_squares / len(col)) ** 0.5

def calculateMeans(path):
    return calculateFeature(path, getMean)

def calculateMedians(path):
    return calculateFeature(path, getMedian)

def calculateStds(path):
    return calculateFeature(path, getStd)