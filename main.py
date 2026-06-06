from services.auth_service import AuthService
from models.user import User
from models.project import Project
from services.project_service import ProjectService

from utils.validation import validate_phone, validate_email
import getpass

auth_service = AuthService()


def projectsList():
    project_service = ProjectService()
    userId = auth_service.current_user["id"]
    while True:
        print("1. Create Project")
        print("2. View Projects")
        print("3. Update Project")
        print("4. Delete Project")
        print("5. Logout")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":

            title = input("Enter title of project: ")
            description = input("Enter description of project: ")
            total_target = input("Enter total target of project: ")
            start_time = input("Enter start time of project: ")
            end_time = input("Enter end time of project: ")

            project = Project(
                title,
                description,
                total_target,
                start_time,
                end_time,
                id=4,
                user_id=userId,
            )
            project_service.add_project(project.to_dict())
        elif choice == "2":
            project_service.view_projects(userId)
        elif choice == "3":
            while True:
                projectId = int(input("Enter the project id to update: "))
                projectInlist = False
                for p in project_service.projects:
                    if p["id"] == projectId:
                        projectInlist = True
                        break
                if not projectInlist:
                    print("Invalid project id. Please try again.")
                    continue
                key = input(
                    "Enter key to update[title, details, total_target, start_time, end_time]: "
                )
                if key not in [
                    "title",
                    "details",
                    "total_target",
                    "start_time",
                    "end_time",
                ]:
                    print("Invalid key. Please try again.")
                    continue
                value = input("Enter value to update: ")
                project_service.update_project(projectId, key, value)
                break

        elif choice == "4":
            while True:
                projectId = int(input("Enter the project id to delete: "))
                projectInlist = False
                for p in project_service.projects:
                    if p["id"] == projectId:
                        projectInlist = True
                        break
                if not projectInlist:
                    print("Invalid project id. Please try again.")
                    continue
                project_service.delete_project(projectId)
                break
        elif choice == "5":
            auth_service.logout()
            break
        elif choice == "6":
            print("")
            print("Goodbye!")
            print("")
            exit()
        else:
            print("Invalid choice. Please try again.")


def main():
    print("")
    print("Welcome to the Project Management System!")
    print("==========================================")

    while True:
        print("1. Login")
        print("2. Register")

        choice = input("Enter your choice: ")
        if choice == "1":
            email = input("Enter your email: ")
            password = getpass.getpass("Enter your password: ")
            if auth_service.login(email, password):
                projectsList()
            else:
                print("Login failed. Please check your email and password. ❌ ")

        elif choice == "2":
            fname = input("Enter your first name: ")
            lname = input("Enter your last name: ")
            while not validate_email(email):
                email = input("Enter your email: ")
                if not validate_email(email):
                    print("Invalid email. Please try again.")
                    continue
            password = getpass.getpass("Enter your password: ")

            mobile = ""
            while not validate_phone(mobile):
                mobile = input("Enter your mobile number: ")
                if not validate_phone(mobile):

                    print("Invalid mobile number. Please try again.")
                    continue

            user = User(
                fname=fname,
                lname=lname,
                email=email,
                password=password,
                mobile=mobile,
                id=auth_service.get_last_user_id() + 1,
            )

            if auth_service.register(user):
                projectsList()
            else:
                print("Registration failed ❌")
        else:
            print("Invalid choice. Please try again. ❌")


if __name__ == "__main__":
    main()
