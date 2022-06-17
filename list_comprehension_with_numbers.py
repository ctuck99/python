import math

def main():

    freqs = [ 120, 150, 180, 210, 240, 270, 300 ]
    
    result = [ math.sqrt(x) for x in freqs ]
    
    rounded_list = [round(num, 4) for num in result]
    
    print(rounded_list)
    
if __name__ == "__main__":
    main()
