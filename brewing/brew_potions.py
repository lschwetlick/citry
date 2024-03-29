
"""
This is a module level docstring
"""

from brewing import potion_class
from brewing import containers
from brewing import cooking
from brewing import inspection


def make_example_potion(student_name="ASPP student"):
    """This function makes an example potion.

    Parameters
    ----------
    student_name : str, optional
        by default "ASPP student"

    Returns
    -------
    potion
        example potion
    """
    my_potion = potion_class.Potion(student_name=student_name)
    # Set up your old kettle and light an eternal flame underneath it.
    my_potion.setup(container=containers.old_kettle, heat_source=cooking.eternal_flame)
    # Simmer for 5 hours.
    cooking.simmer(my_potion, duration=5)
    print(f"You successfully ran make_example_potion, {student_name}, well done :).")
    return my_potion


def make_python_expert_potion(student_name):
    """This function makes a python expert potion.

    Parameters
    ----------
    student_name : str, optional

    Returns
    -------
    potion
        example potion
    """
    print("I am a Python Expert")
    # todo: write this function!
    return


if __name__ == "__main__":
    my_name = 'ASPP student'
    my_potion = make_example_potion(student_name=my_name)
    # Let Snape inspect the potion
    inspection.inspection_by_Snape(potion=my_potion, target_potion='example_potion')
