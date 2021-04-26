from iris_analysis.calculate import calculateMeans, calculateMedians, calculateStds
from iris_analysis.io2.save import saveResults
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

means = calculateMeans(input_file)
medians = calculateMedians(input_file)
stds = calculateStds(input_file)
saveResults(output_file, [means, medians, stds])