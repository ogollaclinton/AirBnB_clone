#!/usr/bin/python3
"""This module defines the hbnb console."""
import cmd
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    return tuple(arg.split())


class HBNBCommand(cmd.Cmd):
    """command interpreter.
    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb)"
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Do nothing if an empty line is recieved."""
        pass

    def do_create(self, arg):
        """Usage: create <class>
        Create a new class instance and display its id.
        """
        arg_l = parse(arg)
        if len(arg_l) == 0:
            print("** class name missing **")
        elif arg_l[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg_l[0])().id)
        storage.save()

    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """
        arg_l = parse(arg)
        dict_object = storage.all()
        if len(arg_l) == 0:
            print("** class name missing **")
        elif arg_l[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_l) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_l[0], arg_l[1]) not in dict_object:
            print("** no instance found **")
        else:
            print(dict_object["{}.{}".format(arg_l[0], arg_l[1])])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id.
        """
        arg_l = parse(arg)
        dict_object = storage.all()
        if len(arg_l) == 0:
            print("** class name missing **")
        elif arg_l[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_l) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_l[0], arg_l[1]) not in dict_object.keys():
            print("** no instance found **")
        else:
            del dict_object["{}.{}".format(arg_l[0], arg_l[1])]
        storage.save()

    def do_all(self, arg):
        """Usage: all /all <class> / <class>.all()
        Display string representations of  instances of a given class.
        instantiated objects if no class is specified."""
        arg_l = parse(arg)
        if len(arg_l) > 0 and arg_l[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            object_list = []
            for objects in storage.all().values():
                if len(arg_l) > 0 and arg_l[0] == objects.__class__.__name__:
                    object_list.append(objects.__str__())
                elif len(arg_l) == 0:
                    object_list.append(objects.__str__())
                    print(object_list)

    def help_create(self):
        """Dislay information about the create command."""
        print("Usage: create <class>")
        print("Create a new class, print its id, and save it to a JSON file")

    def do_quit(self, arg):
        """Return upon receiving quit command."""
        return True

    def help_quit(self):
        """Dispay information about the quit command."""
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """Return upon receiving an EOF signal."""
        print("")
        return True

    def help_EOF(self):
        """Display information about EOF."""
        print("EOF signal to exit the program")

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
        <class>.update(<id>, <attribute_name>, <attribute_value>) or
        <class>.update(<id>, <dictionary>)
        Update class instance of a given id by updating
        a given  dictionary."""
        arg_l = parse(arg)
        dict_object = storage.all()

        if len(arg_l) == 0:
            print("** class name missing **")
            return False
        if arg_l[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(arg_l) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg_l[0], arg_l[1]) not in dict_object.keys():
            print("** no instance found **")
            return False
        if len(arg_l) == 2:
            print("** attribute name missing **")
            return False
        if len(arg_l) == 3:
            try:
                type(eval(arg_l[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(arg_l) == 4:
            objects = dict_object["{}.{}".format(arg_l[0], arg_l[1])]
            if argl[2] in objects.__class__.__dict__.keys():
                val_type = type(objects.__class__.__dict__[arg_l[2]])
                objects.__dict__[arg_l[2]] = val_type(arg_l[3])
            else:
                objects.__dict__[arg_l[2]] = arg_l[3]

        elif type(eval(arg_l[2])) == dict:
            objects = dict_object["{}.{}".format(arg_l[0], arg_l[1])]
            for i, j in eval(argl[2]).items():
                if (i in objects.__class__.__dict__.keys() and
                        type(objects.__class__.__dict__[i]) in {str, int, float}):
                    val_type = type(objects.__class__.__dict__[i])
                    objects.__dict__[i] = valtype(j)
                else:
                    objects.__dict__[i] = j
        storage.save()

    def do_count(self, args):
        """Count number of class instances"""
        count = 0
        for k, v in FileStorage.__objects.items():
            if args == k.split('.')[0]:
                count += 1
                print(count)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
