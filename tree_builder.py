class EmployeeNode:
    """A single employee in the company reporting tree."""

    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class TeamTree:
    """A binary tree that stores the company's reporting structure."""

    def __init__(self):
        self.root = None

    def insert(self, manager_name, employee_name, side, current_node=None):
        """
        Recursively add employee_name as the left or right report of manager_name.

        The first call starts at the root. Recursive calls pass child nodes so the
        search can visit each branch without using a dictionary or list.
        """
        side = side.lower().strip()
        if side not in ("left", "right"):
            print("Error: side must be 'left' or 'right'.")
            return False

        if self.root is None:
            print("Error: add a team lead before adding employees.")
            return False

        # None means this is the first call; begin searching at the root.
        if current_node is None:
            current_node = self.root

        if current_node.name == manager_name:
            if side == "left":
                if current_node.left is not None:
                    print(f"Error: {manager_name} already has a left report.")
                    return False
                current_node.left = EmployeeNode(employee_name)
            else:
                if current_node.right is not None:
                    print(f"Error: {manager_name} already has a right report.")
                    return False
                current_node.right = EmployeeNode(employee_name)

            print(f"Success: {employee_name} added to the {side.upper()} of {manager_name}.")
            return True

        # Search the left branch first, then the right branch.
        if current_node.left is not None:
            if self.insert(manager_name, employee_name, side, current_node.left):
                return True

        if current_node.right is not None:
            if self.insert(manager_name, employee_name, side, current_node.right):
                return True

        # Only print this after both branches have been searched from the root.
        if current_node is self.root:
            print(f"Error: manager '{manager_name}' was not found.")
        return False

    def print_tree(self, node=None, level=0):
        """Recursively print the reporting structure, showing left before right."""
        if node is None:
            if level == 0:
                node = self.root
            if node is None:
                if level == 0:
                    print("The company directory is empty.")
                return

        print(f"{'  ' * level}- {node.name}")
        self.print_tree(node.left, level + 1)
        self.print_tree(node.right, level + 1)


def company_directory():
    """Run the interactive command-line team management menu."""
    company = TeamTree()

    while True:
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")

        choice = input("Choose an option (1–4): ").strip()

        if choice == "1":
            if company.root is not None:
                print("Error: a team lead has already been added.")
                continue
            name = input("Enter team lead's name: ").strip()
            if not name:
                print("Error: employee name cannot be empty.")
                continue
            company.root = EmployeeNode(name)
            print(f"✅ {name} added as the team lead.")

        elif choice == "2":
            if company.root is None:
                print("Error: add a team lead first.")
                continue
            manager = input("Enter the manager's name: ").strip()
            employee = input("Enter the new employee's name: ").strip()
            side = input("Should this employee be on the LEFT or RIGHT of the manager? ").strip()
            if not manager or not employee:
                print("Error: manager and employee names cannot be empty.")
                continue
            company.insert(manager, employee, side)

        elif choice == "3":
            print("\n🌳 Current Team Structure:")
            company.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break

        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    company_directory()


# DESIGN MEMO (200–300 words)
For this assignment, I used a binary tree to represent the company’s team structure. Each employee is stored in an `EmployeeNode` object with a name and two child nodes, `left` and `right`. This allows each manager to have up to two direct reports. The `TeamTree` class manages the structure, and its `root` stores the team lead at the top.

I used recursion in the `insert()` method to search for the manager by name. If the manager is found, the new employee is added to either the left or right side, depending on the user’s choice. If that side is already occupied, the program displays an error message instead of replacing the existing employee. It also lets the user know if the manager cannot be found. These checks help prevent mistakes when building the tree.

The `print_tree()` method also uses recursion. It prints each employee’s name and indents the names of their reports to make the reporting relationships easier to follow. This makes the structure easier to understand than displaying everyone in a flat list.

I kept the terminal menu simple so users can add the team lead, add employees, view the current structure, or exit the program. One limitation is that the tree only allows two direct reports per employee, which may not match every real company. However, this follows the requirements of the assignment and gave me practice using classes, recursion, and binary tree traversal in Python.
