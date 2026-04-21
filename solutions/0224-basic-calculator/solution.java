import java.util.Stack;

class Solution {
    public int calculate(String s) {
        // Our trusty stack to save our game state (result and sign)
        Stack<Integer> stack = new Stack<>();
        
        int result = 0; // The running total
        int num = 0;    // The current number we are building
        int sign = 1;   // 1 represents '+', -1 represents '-'

        // Let's iterate through every single character
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (Character.isDigit(c)) {
                // Build the number. We do c - '0' to convert the char to an actual integer
                // We multiply by 10 to shift digits left (e.g., '1' then '2' becomes 12)
                num = (num * 10) + (c - '0');
                
            } else if (c == '+') {
                // We hit a plus! Time to add the number we just built to our result
                result += sign * num;
                // Reset for the next number
                num = 0;
                sign = 1;
                
            } else if (c == '-') {
                // We hit a minus! Add the number with its sign
                result += sign * num;
                // Reset for the next number, but mark the sign as negative
                num = 0;
                sign = -1;
                
            } else if (c == '(') {
                // Boss room entry! Save our current result and sign to the stack
                stack.push(result);
                stack.push(sign);
                
                // Reset our running totals for the new mini-expression inside the brackets
                result = 0;
                sign = 1;
                
            } else if (c == ')') {
                // Boss defeated! First, finish evaluating the inside of the bracket
                result += sign * num;
                num = 0;
                
                // The top of the stack is the SIGN before the bracket. Multiply it!
                result *= stack.pop();
                
                // The next item on the stack is the RESULT before the bracket. Add it!
                result += stack.pop();
            }
        }
        
        // At the very end of the string, we might have one last number sitting in 'num'
        // Don't forget to add it to the final result!
        if (num != 0) {
            result += sign * num;
        }

        return result;
    }
}
