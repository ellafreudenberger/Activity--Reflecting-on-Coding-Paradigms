def flatten_and_sort(arrays):
    # Flatten the array using list comprehension. flat_list is a new list created to hold the flattened elements from the arrays. Sublist represents each list within the arrays. The outer loop iterates over these sublists. The first occurrence of element represents the variable that will take on the values of the elements within the sublists, and it comes from the innermost loop, which iterates over the elements in the sublists.
    flat_list = [element for sublist in arrays for element in sublist]
    
    # Sort the flattened list in ascending order
    sorted_list = sorted(flat_list)
    
    return sorted_list

# Example usage:
arrays = [[3, 1, 4], [2, 6, 5]]
result = flatten_and_sort(arrays)
print(result)


#How does this solution ensure data immutability?
#It doesn't modifying the original input arrays. It creates new lists (ie. flat_list and sorted_list) throughout the process and the result is a new list.

#Is this solution a pure function? Why or why not?
#Yes, it produces the same output for the same input without any side effects. It operates solely on its input parameters and produces an output and doesn't modify anything outside of its state or perform an additional action. 

#Is this solution a higher order function? Why or why not?
#No, it doesm't take on more functions as arguments or return a function as a result. This function takes an array as an argument.


#Would it have been easier to solve this problem using a different programming style?
#No, functional programming is the most simplified and organized style to transform data because it doesn't cause additional modifications.


#Why is functional programming a helpful paradigm when solving this problem?
#Functional programming's emphasis on purity and immutability is helpful for tasks involving data transformations and sorting because it is clear and concise.

class Podracer:
    #self refers to the instance of the class on which the function is called
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = "repaired"


class AnakinsPod(Podracer):
    def boost(self):
        self.max_speed *= 2


class SebulbasPod(Podracer):
    def flame_jet(self, other_pod):
        other_pod.condition = "trashed"


# Example usage:

# Create a Podracer
pod1 = Podracer(max_speed=500, condition="perfect", price=1500)

# Repair the Podracer
pod1.repair()

# Create Anakin's Podracer
anakins_pod = AnakinsPod(max_speed=800, condition="perfect", price=2000)

# Apply a boost to Anakin's Podracer
anakins_pod.boost()

# Create Sebulba's Podracer
sebulbas_pod = SebulbasPod(max_speed=350, condition="perfect", price=1000)

# Apply a flame jet to Sebulba's Podracer and trash another Podracer
sebulbas_pod.flame_jet(pod1)


#How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
#Encapsulation: Demonstrated - Each class (Podracer, AnakinsPod, and SebulbasPod) bundles attributes and methods into a single unit. The attributes max_speed, condition, and price are encapsulated within each class.
#Abstraction: Partially Demonstrated: The classes closely resemble the real-world entities they represent, but they also abstract the common attributes and behaviors shared by different podracer types.
#Inheritance: Demonstrated: The child classes (AnakinsPod and SebulbasPod) inherit attributes and methods from the parent class (Podracer). 
#Polymorphism: Not Demonstrated: There is the creation of different classes, each with their own specialized methods and attributes, instead of shared methods or attributes for different classes due to their common base class. In Polymorphism, objects of different subclasses can be treated uniformly.