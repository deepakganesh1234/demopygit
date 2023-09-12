#Function to compare protein weights
def compare_protein_weights(weight1, weight2):
    if weight1 > weight2:
        return "Protein 1 is heavier."
    elif weight1 < weight2:
        return "Protein 2 is heavier."
    else:
        return "Both proteins have the same weight."

#Input protein weights from the user
try:
    weight1 = float(input("Enter the weight of Protein 1: "))
    weight2 = float(input("Enter the weight of Protein 2: "))
    
    # Call the function to compare weights
    result = compare_protein_weights(weight1, weight2)
    
    # Display the result
    print(result)

except ValueError:
    print("Invalid input. Please enter valid numeric weights.")
