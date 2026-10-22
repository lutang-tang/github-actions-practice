import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class BankAccountTest {
    private BankAccount account;

    @BeforeEach
    void setUp() {
        // 在每个测试用例执行前，创建一个初始余额为 100 的账户
        account = new BankAccount("ACC001", 100.0);
    }

    @Test
    void testDepositSuccess() {
        account.deposit(50.0);
        assertEquals(150.0, account.getBalance(), "存款后余额应为150");
    }

    @Test
    void testDepositInvalidAmount() {
        Exception exception = assertThrows(IllegalArgumentException.class, () -> {
            account.deposit(-10.0);
        });
        assertEquals("存款金额必须大于0", exception.getMessage());
    }

    @Test
    void testWithdrawSuccess() {
        account.withdraw(40.0);
        assertEquals(60.0, account.getBalance(), "取款后余额应为60");
    }

    @Test
    void testWithdrawInsufficientFunds() {
        Exception exception = assertThrows(ArithmeticException.class, () -> {
            account.withdraw(200.0);
        });
        assertEquals("余额不足", exception.getMessage());
    }
}