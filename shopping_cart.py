class ShoppingCart:
    # write your code here
    def __init__(self, total=0, employee_discount=None, items=[]):
        self.total = total
        self.employee_discount = employee_discount
        self.items = items

    def add_item(self, item_name, price, quantity=1):
        for i in list(range(quantity)):
            self.items.append({"name": item_name, "price": price})
            self.total += price
        return (self.total)

    def mean_item_price(self):
       mean = self.total/len(self.items)
       return mean

    def median_item_price(self):
        prices = sorted([item["price"] for item in self.items])
        n = len(prices)
        if (n%2 == 0):
            med_one = int(n/2)
            med_two = med_one - 1
            median = (prices[med_one] + prices[med_two])/2
            return median
        else:
            med = int(n/2)
            return prices[med]


    def apply_discount(self):
       if self.employee_discount:
           discount = self.employee_discount/100
           discount_tot = self.total * (1 - discount)
           return discount_tot
       else:
           return "Sorry, there is no discount to apply to your cart :("

    def void_last_item(self):
        if self.items:
            removed_item = self.items.pop()
            self.total -= removed_item['price']
        else:
            return "There are no items in your cart!"
        return self.total
