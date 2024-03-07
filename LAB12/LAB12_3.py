"""."""
class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price
    
    def get_weight(self):
        return self.weight
    
    def get_cost(self):
        return self.get_price/self.get_weight

def knapsack(amount, itemList):
    print("Knapsack Size: %0.1f kg" % amount)
    print("===============================")

    # เรียงลิสต์ของสินค้าตามมูลค่าต่อหน่วยน้ำหนัก (มูลค่า/น้ำหนัก) จากมากไปหาน้อย
    sorted_items = sorted(itemList, key=lambda x: x.get_price() / x.get_weight(), reverse=True)

    # สร้างตัวแปรสำหรับเก็บสินค้าที่จะหยิบ
    selected_items = []

    # วนลูปหยิบสินค้าเข้าไปในกระเป๋า
    total_weight = 0
    total_value = 0
    for item in sorted_items:
        if total_weight + item.get_weight() <= amount:
            selected_items.append(item)
            total_weight += item.get_weight()
            total_value += item.get_price()

    # แสดงรายการสินค้าที่หยิบและมูลค่ารวม
    for item in selected_items:
        print(f"{item.get_name()} -> {item.get_weight()} kg -> {item.get_price()} THB")
    print(f"Total: {total_value} THB")

    return selected_items
     


def main():
    import json
    items = []
    num_items = int(input())
    while num_items != 0:
        item_in = json.loads(input())
        items.append(
            Item(item_in['name'], item_in['price'], item_in['weight']))
        num_items = num_items - 1
    knapsack_capacity = float(input())
    knapsack(knapsack_capacity, items)

main()