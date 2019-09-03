
# Variation - How many variations can be done
# k - How many position to be used
# n - The number of all posible positions
# Example - How many 3 digit numbers you can create with the numbers [1, 2, 3, 4, 5] ? ==> V[3|5] = 5*4*3 = 60 variations
# Example Explain - V[k|n] = n*(n-1)*(n-2)...*(n-k+1)



#The function to calculate all variations
def V(n, k):
    #V is our sum of all variations
    v = 1
    #We will try all positions that we can - k
    while k > 0:
        #With the example explain we we see that we need to multiply everytime the n number
        v *= n
        #We also need to decrease it everytime
        n -= 1
        #Our k too
        k -= 1
    return v



Input = input("Example V[k|n]")
#We can't loop forever
while Input != 'stop':
    try:
        k = int(input("k = "))
        n = int(input("n = "))
    #Catching unwanted input
    except:
        print("Try again...")
    else:
        print(f"There are {V(n, k)} variations")
    #We need to inform the user that you can actually stop this
    finally:
        Input = input("Press Enter to continue or type 'stop'...\n")
