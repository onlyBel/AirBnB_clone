#!/usr/bin/python3

"""This is a modulethatcontains the entry point of the command interpreter"""

import sys
import cmd
import models
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    valid_classes = ["User", "City", "State", "Place", "Review",
                     "Amenity", "BaseModel"]

    def do_create(self, line):
        """Creates a new instance of class BaseModel, and saves it to a JSON
        file, and prints the id

        Usage: create <class name>
        """
        args_for_create = line.split()

        if len(args_for_create) == 0:
            print("** class name missing **")
        elif args_for_create[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            class_name = args_for_create[0]
            obj_class = globals()[class_name]
            obj = obj_class()
            obj.save()
            print(obj.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on the
        class name and id

        Usage: show <class name> <id>
        """
        args_for_show = line.split()

        if len(args_for_show) == 0:
            print("** class name missing **")
        elif args_for_show[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args_for_show) < 2:
            print("** instance id missing **")
        else:
            class_name = args_for_show[0]
            uid = args_for_show[1]
            obj_key = f"{class_name}.{uid}"

            if obj_key not in models.storage.all().keys():
                print("** no instance found **")
            else:
                obj = models.storage.all().get(obj_key)
                print(obj)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id.
        The change is saved into the JSON file

        Usage: destroy <class name> <id>
        """
        args_for_destroy = line.split()

        if len(args_for_destroy) == 0:
            print("** class name missing **")
        elif args_for_destroy[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args_for_destroy) < 2:
            print("** instance id missing **")
        else:
            class_name = args_for_destroy[0]
            uid = args_for_destroy[1]
            obj_key = f"{class_name}.{uid}"

            if obj_key not in models.storage.all().keys():
                print("** no instance found **")
            else:
                stored_objs = models.storage.all()
                stored_objs.pop(obj_key)
                models.storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances based
        or not on the class name

        Usage: all
               all <class name>
        """
        args_for_all = line.split()
        stored_objs = models.storage.all()
        print_all = []

        if len(args_for_all) == 0:
            for obj_key in stored_objs.keys():
                obj = stored_objs.get(obj_key)
                print_all.insert(0, obj.__str__())
            print(print_all)
        else:
            if args_for_all[0] not in self.valid_classes:
                print("** class doesn't exist **")
            else:
                class_name = args_for_all[0]
                for obj_key in stored_objs.keys():
                    if obj_key.startswith(class_name):
                        obj = stored_objs.get(obj_key)
                        print_all.insert(0, obj.__str__())
                print(print_all)

    def do_update(self, line):
        """Updates an attribute or adds a new attribute to an existing instance
        of a valid class and saves the change to the JSON file.

        Usage: update <class name> <id> <attribute name> <attribute value>
        """
        args_for_update = line.split()
        stored_objs = models.storage.all()

        if len(args_for_update) == 0:
            print("** class name missing **")
        elif args_for_update[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args_for_update) < 2:
            print("** instance id missing **")
        else:
            class_name = args_for_update[0]
            uid = args_for_update[1]
            obj_key = f"{class_name}.{uid}"

            if obj_key not in stored_objs.keys():
                print("** no instance found **")
            elif len(args_for_update) < 3:
                print("** attribute name missing **")
            elif len(args_for_update) < 4:
                print("** value missing **")
            else:
                attr_name = args_for_update[2]
                attr_value = args_for_update[3]
                obj = stored_objs.get(obj_key)

                if attr_name in obj.__dict__.keys():
                    value_type = type(obj.__dict__.get(attr_name))
                    obj.__dict__[attr_name] = value_type(attr_value)
                else:
                    obj.__dict__[attr_name] = attr_value

                obj.save()

    def do_count(self, line):
        """Counts the number of instances of a class.

        Usage: count <class name>
        """
        args_for_count = line.split()

        if len(args_for_count) == 0:
            print("** class name missing **")
        elif args_for_count[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            stored_objs = models.storage.all()
            class_name = args_for_count[0]
            obj_count = 0

            for key in stored_objs.keys():
                if key.startswith(class_name):
                    obj_count += 1
            print(obj_count)

    def do_quit(self, line):
        """Exits the command interpreter"""
        return True

    def do_EOF(self, line):
        """Exits the command interpreter when an EOF condition is passed"""
        return True

    def emptyline(self):
        """Overrides repeating the last nonempty command after an empty
        line is entered"""
        pass

    def default(self, line):
        valid_methods = {
            "show()": self.do_show,
            "destroy()": self.do_destroy,
            "all()": self.do_all,
            "update()": self.do_update,
            "count()": self.do_count}

        t = line.split(".")
        if len(t) == 2:
            if t[0] in self.valid_classes and t[1] in valid_methods.keys():
                valid_methods[t[1]](t[0])
        else:
            print(f"*** Unknown syntax: {line}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
