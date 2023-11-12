#CS-175
#Victor Davidson
#AverageFromImput
def main():
    pass
    total=0
    count=0
    sales_file = open('numbers.txt', 'r')
    try:
        for line in sales_file:
            try:
                amount = float(line)
                count+=1
                total+=amount
                print(f"I read in {count} number(s) Current number is: {amount:.2f} Total is: {total:.2f}")
            except ValueError:
                print('Error Converting to a number')

        if count > 0:
            average=total/count
            print(f"Average: {average:.1f}")
        sales_file.close()
    except IOError:
        print ("File not found")
    

# Call the main function.
if __name__ == '__main__':
    main()
