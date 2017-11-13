class Product:
    def __init__(self,pId,name,price,quantity):
        """
        Initialises attributes
        """

        self.id = pId
        self.name = name
        self.price = price
        self.quantity = quantity

    def updatePrice(self,new_price):
        """
        Updates the product's price
        """
        if new_price > 0:
            self.price = new_price
        else:
            print "Error! Cannot update price to lower than or equal to zero."

    def updateQuantity(self,new_quantity,isIncrement):
        """
        Allows to update the quantity of the product
        by incrementing or decrementing the quantity
        depending on the value of isIncrement variable.
        """
        if isIncrement is True:
            self.quantity += new_quantity
        elif (self.quantity - new_quantity) >= 0:
            self.quantity -= new_quantity
        else:
            print "Error, cannot reduce further!"

    def getQuantity(self):
        """
        Returns the current quantity of the product.
        """
        return self.quantity

    def viewProduct(self):
        """
        Displays the product's information through print
        """
        print "Product ID: " + str(self.id) + ", Name: " + self.name + ", Price: " + \
        str(self.price) + ", Quantity: " + str(self.quantity)


class Inventory:
    def __init__(self):
        """
        Initialises attribute
        """
        self.listProd = []

    def addProduct(self,pId):
        """
        Add new product to the list
        """
        self.listProd.append(pId)

    def removeProduct(self,pId):
        """
        removes a product from the list
        """
        if pId in self.listProd:
            self.listProd.remove(pId)
        else:
            print "Error. Product is not in the inventory."

    def viewInventory(self):
        """
        Displays inventory list through print
        """
        print self.listProd

if __name__ == '__main__':
    prod1 = Product(1,"colgate",2.20,5)
    print prod1.getQuantity()
    prod1.updateQuantity(2,True)
    prod1.viewProduct()

    invent1 = Inventory()
    invent1.addProduct(1)
    invent1.removeProduct(2)
invent1.viewInventory()
