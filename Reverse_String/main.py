void reverseString(char* s, int sSize) {
    for(int i = 0; i < (sSize/2); i++){
        char tmp = s[sSize - 1 - i];
        s[sSize - 1 - i] = s[i];
        s[i] = tmp;
    }
}
