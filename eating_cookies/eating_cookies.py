'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Your code here
    if n < 0:
        return 0
    if n <= 1:
        return 1
    else:
        return eating_cookies(n-1)+eating_cookies(n-2)+eating_cookies(n-3)

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5 #13


    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")

# 1:1, 2:2, 3:4, 4:7, 5:13, 10:274
# 1:1^?
# 2:2^1 or 1^? + 1^?
# 3:2^2 or 3^1 + 1^?
# 4:c3+c2+c1
# 5:c4+c3+c2
