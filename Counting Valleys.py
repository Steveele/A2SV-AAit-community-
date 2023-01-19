def countingValleys(steps, path):
    # Write your code here
    altitude=0
    valley=0
    di={"U":1 , "D":-1}
    for i in path:
        altitude+=di[i]
        if altitude==0 and i=="U":
            valley+=1
    return valley
        