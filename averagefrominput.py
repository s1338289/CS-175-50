#CS-175
#Victor Davidson
#AverageFromImput

def main():
    pass
    total=0
    count=0
    sales_file = open('numbers.txt', 'r')
    for line in sales_file:
        amount = float(line)
        count+=1
        total+=amount
        print(f"I read in {count} number(s) Current number is: {amount:.2f} Total is: {total:.2f}")

    if count > 0:
        average=total/count
        print(f"Average: {average:.1f}")

    
    # Close the file.
    sales_file.close()

# Call the main function.
if __name__ == '__main__':
    main()
