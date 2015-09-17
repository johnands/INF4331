def extract(filename):
    """store test names and CPU times in dictionary"""   
    infile = open(filename, 'r')
    tests = {}
    for line in infile:
        if "CPU" in line:
            words = line.split()
            name = words[1]       
            CPU = float(words[-1])
            if name in tests:
                tests[name].append(CPU)
            else:
                tests[name] = [CPU]
    return tests

def compute(tests):
    """
    compute average, min and max CPU time  
    for each test and print to screen
    """
    for test in tests:
        cpu_times = tests[test]
        minimum = min(cpu_times)
        maximum = max(cpu_times)
        average = sum(cpu_times)/len(cpu_times)

        print """
              Test name: %s
              CPU time:  %.1f s (min)
                         %.1f s (avg)
                         %.1f s (max)

              """ % (test, minimum, average, maximum)

# main
tests = extract('data.log')
compute(tests)


