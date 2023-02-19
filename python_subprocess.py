import subprocess #สำหรับ รัน terminal command

if __name__ == "__main__":
    ## basic
    # subprocess.run(["ls", "-ltr"])
    # subprocess.run(["python", "python_script101.py", "--x","8"])
    
    ## use output of subprocess
    
    sum = 0 
    for i in range(50):
        if i % 2 != 0 :
            
            process1 = subprocess.Popen(["python", "python_script101.py", "--x",f'{i}'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = process1.communicate()
            print(out.decode('utf-8'))

                #ผลรวม xt= xt*2
            sum += (i*2)
            
            
    print(f'Summation of xt = {sum}')
    


    #HW สั่งรัน python_script101.py 50 รอบ โดย x = 1,3,5,7,... 
    #แล้วให้เอา output ของ xt มารวมกัน แล้ว print ออกมา