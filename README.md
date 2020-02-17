# Greenflag
Simple Django API To Sum Positive Integer Range

sums up a range of numbers from an api endpoint \
assumptions: \
api = '/total?range= <int:positive integer>' <- inclusive \
e.g. range=4 sums up 1, 2, 3, 4 inclusive \
else if no 'range' then returns 0 

** use \
http://localhost:8000/total?range=4"

returns: \
JSON object {'total': 10}
