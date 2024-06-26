class Height(object):
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __str__(self):
        output = str(self.feet) + " feet, " + str(self.inches) + " inches"
        return output

    def __add__(self, other):
        # Converting both objects' heights into inches
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = other.feet * 12 + other.inches

        # Adding them up
        total_height_inches = height_A_inches + height_B_inches

        # Getting the output in feet
        output_feet = total_height_inches // 12

        # Getting the output in inches
        output_inches = total_height_inches - (output_feet * 12)

        # Returning the final output as a new Height object
        return Height(output_feet, output_inches)

    def __sub__(self, other):
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = self.feet + 12 + self.inches

        # Subtracting them 
        total_height = height_A_inches - height_B_inches

        # Getting the output in feets
        output_feet = total_height // 12

        # Getting the output in inches
        output_inches = total_height - (output_feet * 12)

        # Returning the final output as a new Height object
        return Height(output_feet, output_inches)

print('Height(5, 10) + Height(4, 10)')
person_A_height = Height(5, 10)
person_B_height = Height(4, 10)
height_sum = person_A_height + person_B_height

print("Total height Sum:", height_sum)


print('Height(5, 10) - Height(3, 9)')
person_A_height = Height(5, 10)
person_B_height + Height(3, 9)
height_sub = person_A_height - person_B_height

print('Total height Sub: ', height_sub)