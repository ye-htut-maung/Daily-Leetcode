class Solution {
  public String shiftingLetters(String s, int[] shifts) {
    char[] char_arr = s.toCharArray();
    int cumulativeAdd = 0;
    for (int i = shifts.length - 1; i >= 0; i--) {
      cumulativeAdd = (cumulativeAdd + shifts[i]) % 26;
      char_arr[i] = (char) ((((char_arr[i] + cumulativeAdd) - 97) % 26) + 97);

    }

    return new String(char_arr);
  }
}