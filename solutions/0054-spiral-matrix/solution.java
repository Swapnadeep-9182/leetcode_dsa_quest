class Solution {
public List spiralOrder(int[][] matrix) {
List result = new ArrayList<>();
if (matrix == null || matrix.length == 0) return result;

int rowBegin = 0;
int rowEnd = matrix.length - 1;
int columnBegin = 0;
int columnEnd = matrix[0].length - 1;

while (rowBegin <= rowEnd && columnBegin <= columnEnd) {
// Traverse Right (7:07)
for (int i = columnBegin; i <= columnEnd; i++) {
result.add(matrix[rowBegin][i]);
}
rowBegin++;

// Traverse Down (8:04)
for (int i = rowBegin; i <= rowEnd; i++) {
result.add(matrix[i][columnEnd]);
}
columnEnd--;

if (rowBegin <= rowEnd) {
// Traverse Left (9:05)
for (int i = columnEnd; i >= columnBegin; i--) {
result.add(matrix[rowEnd][i]);
}
}
rowEnd--;

if (columnBegin <= columnEnd) {
// Traverse Up (10:14)
for (int i = rowEnd; i >= rowBegin; i--) {
result.add(matrix[i][columnBegin]);
}
}
columnBegin++;
}
return result;
}
}
