#f=open("file5.txt","x")
# f=open("file4.txt","w")
# f.write("Hello.....")
# f.writelines(["\nmenu\nidli\ndosa\nvada pav "])
# f.close()
f = open("file4.txt", "r")  
content = f.read() 
# Read the content
print(content)                # Print the content, not the file object
f.close()

