class OrderSystem:
    def __init__(self):
        self.cart = []
        self.discount_rate = 0.0  # 默认无折扣

    def add_item(self, name, price, quantity=1):
        """添加商品到购物车"""
        if price < 0 or quantity <= 0:
            raise ValueError("价格不能为负数，且数量必须大于0")
        self.cart.append({"name": name, "price": price, "quantity": quantity})
        return True

    def calculate_total(self):
        """计算购物车总价"""
        total = sum(item["price"] * item["quantity"] for item in self.cart)
        return round(total, 2)

    def apply_discount(self, rate):
        """应用折扣，例如输入 0.1 代表打9折（减去10%）"""
        if not (0 <= rate <= 1):
            raise ValueError("折扣率必须在 0 到 1 之间")
        self.discount_rate = rate

    def checkout(self, user_level="normal"):
        """结账，包含用户等级额外优惠"""
        if not self.cart:
            raise Exception("购物车为空，无法结账")

        total = self.calculate_total()

        # 应用普通折扣
        total = total * (1 - self.discount_rate)

        # VIP 用户额外 95折
        if user_level == "vip":
            total = total * 0.95

        return round(total, 2)