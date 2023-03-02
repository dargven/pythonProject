a = 'asdsadAASDADSafsdfdafssifjAJFASOIJDIoajsdisajafoisjAIDJAIFJWQIDPSADIasfjasfksdASKDHahdssajfaJAKDJAShjfka'
cnt = 0
for i in range(len(a)):
    if a[i].isupper():
        cnt+=1
print(cnt)