class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder sb = new StringBuilder();

        // Filter out non-alphanumeric characters and convert to lowercase
        for (char i : s.toCharArray()) {
            if (Character.isLetterOrDigit(i)) {
                sb.append(Character.toLowerCase(i));
            }
        }

        // Get the filtered string
        String filteredString = sb.toString();

        // Reset pointers for the filtered string
        int left = 0;
        int right = filteredString.length() - 1;

        // Check if the filtered string is a palindrome
        while (left <= right) {
            if (filteredString.charAt(left) != filteredString.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }

        return true;
    }
}