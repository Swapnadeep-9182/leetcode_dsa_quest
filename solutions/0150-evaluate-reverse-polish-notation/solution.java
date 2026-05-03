class Solution {
    public int evalRPN(String[] tokens) {
        // 1. Store Integers instead of Strings to make math easier
        Stack<Integer> stack = new Stack<>();

        // 2. token must be a String since tokens is a String array
        for(String token : tokens) {
            
            // 3. Use .equals() for String comparison in Java
            if(token.equals("+") || token.equals("-") || token.equals("*") || token.equals("/")) {
                
                // 4. Use the lowercase 'stack' instance, and declare 'int'
                int operand2 = stack.pop();
                int operand1 = stack.pop();
                
                // 5. Declare result outside the if-blocks so it stays in scope
                int result = 0;

                if(token.equals("+")){
                    result = operand1 + operand2;
                }
                if(token.equals("*")){
                    result = operand1 * operand2;
                }
                if(token.equals("-")){
                    result = operand1 - operand2;
                }
                if(token.equals("/")){
                    result = operand1 / operand2;
                }

                stack.push(result);
            } else {
                // 6. Correct Java method to parse a string into an integer
                stack.push(Integer.parseInt(token));
            }
        }
        
        return stack.pop();
    }
}
