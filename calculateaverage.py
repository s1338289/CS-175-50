#CS-175
#Victor Davidson
#CalculateAverage.py

def main ():
            Repeat = "yes"
            while Repeat=="yes":
                scores = []

                for x in range(5):
                    scores.append(int(input("Enter test score"+str(x+1)+": ")))

                print("Score","NumericLetterGrade")
                print("------------------------")

                for x in scores:
                    print(x,determine_grade(x))

                avg = calc_average(scores[0], scores[1], scores[2], scores[3], scores[4])

                print("\nAverage score =",avg)
                
                Repeat = input("Enter 'yes' if you would like to do another calculation:")
                Repeat = Repeat.lower()
            print("Thank you for using this program")   


def calc_average(n1,n2,n3,n4,n5):
    return (n1+n2+n3+n4+n5)/5

def determine_grade(value):
    if value < 60:
        letter = 'F'
    elif value < 70:
        letter = 'D'
    elif value < 80:
        letter = 'C'
    elif value < 90:
        letter = 'B'
    else:
        letter = 'A'

    return letter


if __name__ == '__main__':
    main()

            
                  
            

            
                
                        
