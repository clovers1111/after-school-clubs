from repository import ClubRepository

from views import HomeView


# Controller sits directly under the view and
# manages the view's state directly
class HomeController:
    clubs_repository = None
    home_view = None


    def __init__(self, club_repository: ClubRepository, home_view: HomeView=None):
        self.clubs_repository = club_repository
        self.home_view = home_view


    def fetch_clubs(self):
        clubs = self.clubs_repository.find_all_clubs()
        self.home_view.set_clubs(clubs)

    def set_home_view(self, home_view: HomeView):
        self.home_view = home_view