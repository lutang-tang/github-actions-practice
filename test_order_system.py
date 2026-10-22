import pytest
from order_system import OrderSystem

@pytest.fixture
def empty_order():
    """创建一个空的订单系统实例供测试使用"""
    return OrderSystem()

def test_add_item_success(empty_order):
    """测试正常添加商品"""
    assert empty_order.add_item("苹果", 5.0, 3) == True
    assert len(empty_order.cart) == 1
    assert empty_order.calculate_total() == 15.0

def test_add_item_invalid_price(empty_order):
    """测试添加商品时价格非法的情况，期望抛出 ValueError"""
    with pytest.raises(ValueError, match="价格不能为负数"):
        empty_order.add_item("香蕉", -2.0, 1)

def test_calculate_total_multiple_items(empty_order):
    """测试多个商品的总价计算"""
    empty_order.add_item("鼠标", 99.9, 1)
    empty_order.add_item("键盘", 199.5, 2)
    assert empty_order.calculate_total() == 498.9

def test_apply_valid_discount(empty_order):
    """测试应用合法折扣"""
    empty_order.apply_discount(0.2) # 打8折
    assert empty_order.discount_rate == 0.2

def test_apply_invalid_discount(empty_order):
    """测试应用非法折扣，期望抛出 ValueError"""
    with pytest.raises(ValueError, match="折扣率必须在 0 到 1 之间"):
        empty_order.apply_discount(1.5)

def test_checkout_empty_cart(empty_order):
    """测试空购物车结账，期望抛出 Exception"""
    with pytest.raises(Exception, match="购物车为空"):
        empty_order.checkout()

def test_checkout_vip_user(empty_order):
    """测试 VIP 用户结账逻辑：原价100，打9折(90)，VIP再95折(85.5)"""
    empty_order.add_item("T恤", 100, 1)
    empty_order.apply_discount(0.1)
    assert empty_order.checkout(user_level="vip") == 85.5

def test_checkout_normal_user(empty_order):
    """测试普通用户结账逻辑"""
    empty_order.add_item("书籍", 50, 2)
    assert empty_order.checkout() == 100.0