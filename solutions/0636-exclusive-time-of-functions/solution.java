class Solution {
    public int[] exclusiveTime(int n, List<String> logs) {
        int[] result = new int[n];
        Deque<Integer> stack = new ArrayDeque<>();
        int prevTime = 0;
        for(String log : logs){
            String[] parts = log.split(":");

            int id = Integer.parseInt(parts[0]);
            String action = parts[1];
            int time = Integer.parseInt(parts[2]);

            if(action.equals("start")){
                if(!stack.isEmpty()){
                    int runningId = stack.peek();
                    result[runningId] += (time - prevTime);
                    prevTime = time;
                }
                stack.push(id);
                prevTime = time;
            }else if(action.equals("end")){
                int finishingId = stack.pop();
                result[finishingId] += (time - prevTime + 1);
                prevTime = time + 1;
            }
        }
        return result;
    }
}
