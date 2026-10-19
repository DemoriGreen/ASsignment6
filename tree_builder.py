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
# Recursive insertion works by checking the current employee node to see whether
# that person is the requested manager. If the names match, the method checks the
# selected side and creates a new EmployeeNode only when that branch is empty.
# Otherwise, it calls itself on the left and right children. Each recursive call
# examines a smaller part of the company directory, so the search moves down the
# hierarchy until it finds the manager or reaches the end of the available paths.
# The root is used as the starting point for the first call.
#
# One challenge was handling an empty child without confusing it with the initial
# call. The method uses current_node=None to signal that the search should begin
# at the root, while recursive calls pass a specific child node. Another challenge
# was preventing employees from overwriting existing reports. Checking whether the
# requested side is already occupied preserves the tree and provides a useful error
# message. Searching both branches also makes it possible to find managers who are
# not at the top of the organization.
#
# Trees are useful whenever data has a natural hierarchy. A company directory is
# a clear example because each manager can supervise lower-level employees, and
# each employee has a defined place in the reporting structure. Trees can also
# represent file systems, website document structures, decision processes, and
# category menus. Compared with a flat list, a tree makes parent-child relationships
# explicit and can support efficient searching when its structure is designed for
# that purpose. This implementation is a binary tree, so each employee can have
# at most two direct reports. Although that is a project requirement rather than a
# universal business rule, the same node-based approach can be extended to support
# more children in a real organizational directory.
