from github2.core import BaseData, GithubCommand, Attribute, DateAttribute
from github2.users import User
from github2.repositories import Repository
import urllib

class Team(BaseData):
    """ A team """
    name = Attribute("The team name")
    id = Attribute("The team id")
    permission = Attribute("The permissions the team has")

    def __repr__(self):
        return "<Team: %s>" % self.name


class Teams(GithubCommand):
    """ Github command for operating on teams """
    domain = "teams"

    def add_member(self, team_id, username):
        """Adds a member to a team."""
        return self.make_request(str(team_id), "members", method="POST",
                                 post_data={'name': username})

    def remove_member(self, team_id, username):
        """Removes a member from a team."""
        return self.make_request(str(team_id), "members", method="DELETE",
                                 query={'name': username})

    def members(self, team_id):
        """ Returns the list of members of a team """
        return self.get_values(str(team_id), "members", filter="users", 
            datatype=User)

    def repositories(self, team_id):
        return self.get_values(str(team_id), "repositories", filter='repositories',
            datatype=Repository)
