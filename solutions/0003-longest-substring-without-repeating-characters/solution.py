class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''আমরা এখানে ২টো pointer (বা আঙুল) ব্যবহার করব— left আর right। আর এই টেকনিকটাকে বলে Sliding Window!

            ভাবো, তোমার কাছে একটা রাবার ব্যান্ড (window) আছে।

            left আর right দুটো pointer-ই শুরুতে ০ (zero) index-এ থাকবে।

            right pointer-টা ডানদিকে এক এক ধাপ করে এগোবে আর চেক করবে: "এই ক্যারেক্টারটা কি আমার Set-এ আছে?"

            যদি না থাকে: খুব ভালো! তুমি ক্যারেক্টারটাকে Set-এ ঢুকিয়ে নেবে। তোমার রাবার ব্যান্ডটা (উইন্ডো) বড় হবে, আর তুমি হিসাব রাখবে যে এখনও পর্যন্ত সবচেয়ে বড় সাইজ কত হলো।

            যদি থাকে (মানে ডুপ্লিকেট পেয়ে গেছ): বিপদ! তখন তুমি left pointer-টাকে এক এক ধাপ করে এগোতে শুরু করবে আর Set থেকে বাঁদিকের ক্যারেক্টারগুলো একটা একটা করে মুছতে থাকবে, ঠিক যতক্ষণ না ওই ডুপ্লিকেট ক্যারেক্টারটা Set থেকে বেরিয়ে যায়।'''
        left = 0
        max_length = 0
        char_set = set()

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])

            window = right - left + 1

            max_length = max(max_length,window)

        return max_length
