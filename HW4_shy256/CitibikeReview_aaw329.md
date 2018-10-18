## Review of Duke's Citi Bike project proposal

The original proposal can be found here:
[Assignment2_shy256](https://github.com/sunghoonyang/PUI2018_shy256/blob/master/HW4_shy256/Assignment2_shy256.ipynb)

 - The null and alternative are correctly formulated, since both H0 and H1 are logical and encompass all possible values. These are specific, and testable (e.g. ride durations are at least 7 minutes, and end stations were at least 500 meters away from start stations).

 - The data, as wrangled, does support the project because it contains the calculated average speed and gender. These are the two data points necessary to evaluate the hypotheses.

 - An appropriate statistical test for the hypotheses would be an unpaired t-test. Based on this [flowchart for selecting a stastical test](http://abacus.bates.edu/~ganderso/biology/resources/stats_flow_chart_v2014.pdf), it is appropriate because we're looking at differences in means of continuous data (speed) among two groups (male and female). An unpaired test would be appropriate because each data point is unrelated to other data points in the other group (i.e. we can assume one individual is not in the same group). 

 - One additional noteworthy point is that the distance used to calculate speed is not the distance of the path traveled by the Citi Bike rider, but instead the distance between the start station and end station. It would be better to use the distance of the actual path traveled if it were available, but the distance between stations is probably worthy of an approximation for the actual distance traveled. Error will increase the further the rider deviates from the straight line between the start and end stations.
