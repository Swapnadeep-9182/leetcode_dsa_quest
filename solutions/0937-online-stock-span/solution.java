import java.util.*;

class StockSpanner {
    // 1. Use generics to specify the stack stores int arrays
    private Stack<int[]> stack;

    public StockSpanner() {
        stack = new Stack<>();
    }
    
    public int next(int price) {
        int span = 1;

        // 2. Logic fix: The problem usually requires prices GREATER THAN OR EQUAL TO
        // top of stack to be popped. Changed < to <=
        while(!stack.isEmpty() && stack.peek()[0] <= price) {
            span += stack.pop()[1];
        }

        // 3. Typo fix: Changed 'new inr[]' to 'new int[]'
        stack.push(new int[]{price, span});

        return span;
    }
}


/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner obj = new StockSpanner();
 * int param_1 = obj.next(price);
 */
