from typing import TYPE_CHECKING

from ares import ManagerMediator
from ares.managers.manager import Manager

if TYPE_CHECKING:
    from ares import AresBot


class WorkerRushManager(Manager):

    def __init__(
        self,
        ai: "AresBot",
        config: dict,
        mediator: ManagerMediator,
    ) -> None:
        """Manager to handle worker rushing

        Parameters
        ----------
        ai :
            Bot object that will be running the game
        config :
            Dictionary with the data from the configuration file
        mediator :
            ManagerMediator used for getting information from other managers.
        """
        super().__init__(ai, config, mediator)

    def initialise(self) -> None:
        """
        Don't have to implement this method
        Runs once game is loaded / first frame

        Returns
        -------

        """
        pass

    async def update(self, iteration: int) -> None:
        for worker in self.ai.workers:
            worker.attack(self.ai.enemy_start_locations[0])