# Lesson 5
initial_money = float(input("enter starting amount "))
cookies_sold = input("enter cookies sold as b for big and c for normal ")
big_cookies = cookies_sold.count("b") 
normal_cookies = cookies_sold.count("c")

total_cookies = (big_cookies + normal_cookies)
bigc_sale = (big_cookies * 2)
normalc_sale = (normal_cookies * 1.25)
bigc_profit = (bigc_sale - (big_cookies * 0.75))
normalc_profit = (normalc_sale - (normal_cookies * 0.50))
total_profit = (normalc_profit + bigc_profit)
print (f"the total number of cookies sold are {total_cookies}")
print (f"the profit is {total_profit}")
print (f"the total amount of money is {total_profit + initial_money}")
