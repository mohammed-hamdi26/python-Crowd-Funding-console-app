class Project:
    def __init__(self, title, details, total_target, start_time, end_time,user_id,id):
        self.title = title
        self.details = details
        self.total_target = total_target
        self.start_time = start_time
        self.end_time = end_time
        self.user_id = user_id
        self.id = id

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "details": self.details,
            "total_target": self.total_target,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "user_id": self.user_id
        }