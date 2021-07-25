from src.api.models.seeds.seed import Seed


class AttachmentSeed(Seed):

    def __init__(self, file, included_seeds, issue_id):
        self.id = None
        self.file = file
        self.included_seeds = included_seeds
        self.issue_id = issue_id

    def attributes(self):
        return {
            'file': self.file
        }

    def type(self):
        return 'attachments'

    def __str__(self):
        return f"AttachmentSeed<id={self.id}, file={self.file}, " \
               f"included_seeds={self.included_seeds}, issue_id={self.issue_id}>"

    def __repr__(self):
        return f"AttachmentSeed<id={self.id}, file={self.file}, " \
               f"included_seeds={self.included_seeds}, issue_id={self.issue_id}>"
