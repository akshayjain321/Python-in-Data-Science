#This is a program to display a logical and a runtime error

#Write a program to calculate discount on a product item and then add fixed surcharge on the discounted price

#calculate discount on product item

product_price = int(input("Enter price of the product: "))
discount = int(input("Enter discount in %: "))
discounted_price = product_price - (product_price % discount)
print(f"Discounted price is: {discounted_price}")

#Logical error: The correct formula to calcuate discounted price should be:
# product_price - (product_price * (discount/100))

#calculate surcharge on product item

surcharge = input("Enter fixed surcharge amount: ")
final_price = discounted_price + surcharge
print(f"Final price is: {final_price}")

#Runtime error: surcharge should be casted into an integer (or float) as it is being added to another number


