from controllers import *
route = [
    (
        r"/",
        home.homeHandler
    ),
    (
        r"/api/do/droplets/list",
        doActions.listDropletsHandler
    ),
    (
        r"/api/do/droplet/create",
        doActions.createDropletHandler
    ),
    (
        r"/api/do/details",
        doActions.accountDetailHandler
    ),
    (
        r"/api/github/pull",
        githubActions.pullGitHandler
    ),
(
        r"/api/github/status",
        githubActions.repoStatusHandler
    ),
    (
        r"/api/github/logs",
        githubActions.repoLogsHandler
    ),
    (
        r"/chat",
        botController.chatHandler
    )
]
