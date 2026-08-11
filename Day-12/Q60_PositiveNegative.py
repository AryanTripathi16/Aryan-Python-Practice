# Question:Write a Python program to separate positive and negative numbers from a list.

def separate_numbers(numbers):
    positives = []
    negatives = []

    for num in numbers:
        if num >= 0:
            positives.append(num)
        else:
            negatives.append(num)

    return positives, negatives


sample_list = [10, -5, 23, -12, 0, -3, 8]
pos_list, neg_list = separate_numbers(sample_list)

print("Positive numbers:", pos_list)
print("Negative numbers:", neg_list)
