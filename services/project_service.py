from utils.file_handler import load_data, save_data


class ProjectService:
    def __init__(self):
        self.projects = load_data("json/projects.json")

    def add_project(self, project):
        self.projects.append(project)
        save_data("json/projects.json", self.projects)
        print("Project added successfully ✅")

    def update_project(self, id, key, value):
        for p in self.projects:
            if p["id"] == id:
                p[key] = value
                print("after update", p)
                break
        save_data("json/projects.json", self.projects)
        print("Project updated successfully ✅")

    def delete_project(self, id):
        for p in self.projects:
            if p["id"] == id:
                self.projects.remove(p)
                break

        save_data("json/projects.json", self.projects)
        print("Project deleted successfully ✅")

    def view_projects(self, userId):
        print(
            f"{'id':<10}  {'title':<10}  {'details':<10}  {'total_target':<10}  {'start_time':<10}  {'end_time':<10}"
        )
        for p in self.projects:
            if p["user_id"] == userId:
                print(
                    f"{p['id']:<10}  {p['title']:<10}  {p['details']:<10}  {p['total_target']:<10}  {p['start_time']:<10}  {p['end_time']:<10}"
                )

        else:
            print("You don't have any projects")
