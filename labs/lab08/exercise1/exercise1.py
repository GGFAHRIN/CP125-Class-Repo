# Lab 08 Exercise 1: Simple Score Filter
# Write your code below:
def filter_passing_scores(input_file, output_file):
    count = 0
    
    infile = open(input_file, "r")
    outfile = open(output_file, "w")
    
    lines = infile.readlines()
    
    for line in lines:
        line = line.strip()
        parts = line.split(" ")   # split by space
        
        student_id = parts[0]
        score = int(parts[1])

        if score >= 80:
            outfile.write(student_id + " " + str(score) + "\n")
            count = count + 1
    
    infile.close()
    outfile.close()

    return count


# Test your code here
result = filter_passing_scores("labs/lab08/exercise1/data/scores.txt", "labs/lab08/data/passing.txt")
print(f"Passing students: {result}")
