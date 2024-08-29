my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#list[start:end:step]
print (my_list[2:-1:1])                                #o/p: [2, 3, 4, 5, 6, 7, 8]
print(my_list[-1:2:-1])                                #o/p: [9, 8, 7, 6, 5, 4, 3]



sample_url ='http://coreyms.com'
#Reverse the sample_url
print(sample_url[::-1])                               #o/p: moc.smyeroc//:ptth
#get the top level domain
print(sample_url[-4:])                                #o/p: .com
#url without the http:/ 
print(sample_url[7:])                                 #o/p: coreyms.com
#url without the http:// or the top level domain
print(sample_url[7:-4])                               #o/p: coreyms
