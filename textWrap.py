import textwrap

def wrap(string, max_width):
  
    ans=""
    count=0
    for i in string :
        ans=ans+i
        count+=1
    
        if count ==max_width:
            ans=ans+"\n"
            count=0
      
          
    return ans

if __name__ == '__main__':